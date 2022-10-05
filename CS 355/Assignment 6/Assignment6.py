# CSCI 355/655
# Summer 2022
# Assignment 7 - Flask
# Justin Day


import pymysql
import requests
from bs4 import BeautifulSoup
import webbrowser
import os


def read_password():
    with open("password.txt") as file:  # Use file to refer to the file object
        password = file.read().strip()
    return password


def connect_to_db():
    password = read_password()
    conn = pymysql.connect(host="mars.cs.qc.cuny.edu", user="daju9399", passwd=password, database="daju9399", port=3306)
    # cursor = conn.cursor()
    # cursor.execute("SHOW DATABASES")
    # for row in cursor:
    #     print(row)
    return conn


def get_state_data():
    url = 'https://www.thespreadsheetguru.com/blog/list-united-states-capitals-abbreviations'
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    items = soup.find_all('p')
    state_data = ""
    capital_data = ""
    abbr_data = ""

    for item in items:
        if "Alabama" in item:
            state_data = str(item)
        if "NJ" in item:
            abbr_data = str(item)
        if "Juneau" in item:
            capital_data = str(item)

    state_data = state_data[state_data.index("Alabama"):].split("<br/>")
    abbr_data = abbr_data[abbr_data.index("AL"):].split("<br/>")
    capital_data = capital_data[capital_data.index("Montgomery"):].split("<br/>")

    state_data[49] = state_data[49].replace('</p>', '')
    abbr_data[49] = abbr_data[49].replace('</p>', '')
    capital_data[49] = capital_data[49].replace('</p>', '')

    states = [[state_data[i], abbr_data[i], capital_data[i]] for i in range(50)]

    return states    # data_iterator = iter(items)


def insert_state_data(states):
    conn = connect_to_db()
    cursor = conn.cursor()
    for state in states:
        name = state[0]
        ref ="https://en.wikipedia.org/wiki/" + name.replace(' ', '_') + '_(state)'
        query = f"update states modify set link='{ref}'  where state_name ='{name}'"
        print(query)
        cursor.execute(query)
    conn.commit()
    conn.close()


def select_states():
    conn = connect_to_db()
    cursor = conn.cursor()
    query = "SELECT * FROM states ORDER BY state_name"
    cursor.execute(query)
    rows = cursor.fetchall()
    states = []
    for row in rows:
        print(row)
        states.append(row)

    conn.commit()
    conn.close()

    return states


def write_file(filename, message):
    f = open(filename, 'w')
    f.write(message)
    f.close()


def open_file_in_browser(filename):
    url = 'file:///' + os.getcwd() + '/' + filename
    webbrowser.open_new_tab(url)


TAG_DOCTYPE = '<!DOCTYPE html>'
TAG_HTML = 'html'
TAG_HEAD = 'head'
TAG_BODY = 'body'
TAG_TABLE = 'table'
TAG_TH = 'th'
TAG_TD = 'td'
TAG_TR = 'tr'
TAG_PAR = 'p'
TAG_H1 = 'h1' # HTML supports six default heading tags H1, H2, H3, H4, H5, and H6
TAG_BR = 'br'
TAG_LINK = 'link'
TAG_A = 'a'


def create_element(tag, content, attributes="", end_tag=True):
    element = "<" + tag + " " + attributes + ">"
    if end_tag:
        element += content + "</" + tag + ">"

    return element + "\n"


def create_elements(tag, list_contents):
    elements = ""
    for content in list_contents:
        elements += create_element(tag, content)

    return elements


def create_table(headers, data):
    rows = create_elements(TAG_TH, headers)
    for datum in data:
        name = datum[1]
        href = 'href = "https://en.wikipedia.org/wiki/' + name.replace(' ', '_') + '_(state)' + '"'
        name = datum[0]
        a = create_element(TAG_A, name, href, True)
        tda = create_element(TAG_TD, a)
        tds = create_elements(TAG_TD, datum[1:])
        row = create_element(TAG_TR, tda + tds)
        rows += row

    table = create_element(TAG_TABLE, rows)
    return table


def main():
    connect_to_db()
    # states = get_state_data()
    # insert_state_data(states)
    states = select_states()
    headers = ['Abbreviation', 'State', 'Capital']
    table = create_table(headers, states)
    heading = create_element(TAG_H1, "Justin's United States Data From Database")

    link_attributes = 'rel = "stylesheet" href = "MyStyle.css"'
    link = create_element(TAG_LINK, '', link_attributes, end_tag=False)

    head = create_element(TAG_HEAD, link)
    body = create_element(TAG_BODY, heading + table) #+ TAG_BR
    message = create_element(TAG_HTML, head + body)
    write_file('states.html', message)
    open_file_in_browser('states.html')


if __name__ == '__main__':
    main()
