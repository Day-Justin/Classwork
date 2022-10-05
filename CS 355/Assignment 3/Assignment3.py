# CSCI 355/655
# Summer 2022
# Assignment 3 - HTML and CSS
# Justin Day


import webbrowser
import os
import requests
# import html5lib
from bs4 import BeautifulSoup


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
        name = datum[0]
        href = 'href = "https://en.wikipedia.org/wiki/' + name.replace(' ', '_') + '_(state)' + '"'
        a = create_element(TAG_A, name, href, True)
        tda = create_element(TAG_TD, a)
        tds = create_elements(TAG_TD, datum[1:])
        row = create_element(TAG_TR, tda + tds)
        rows += row

    table = create_element(TAG_TABLE, rows)
    return table


def write_file(filename, message):
    f = open(filename, 'w')
    f.write(message)
    f.close()


def open_file_in_browser(filename):
    url = 'file:///' + os.getcwd() + '/' + filename
    webbrowser.open_new_tab(url)


def scrape_state_data():
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
    states = [[state_data[i], abbr_data[i], capital_data[i]] for i in range(50)]
    return states    # data_iterator = iter(items)
    # # This loop will keep repeating as long as there is data available in the iterator
    # while True:
    #     try:
    #         country = next(data_iterator).text
    #         confirmed = next(data_iterator).text
    #         deaths = next(data_iterator).text
    #         continent = next(data_iterator).text
    #         population = 0  # placeholder - will be replaced in next task
    #         # For 'confirmed' and 'deaths', remove the commas and convert to int
    #         data.append((
    #             country,
    #             int(confirmed.replace(',', '')),
    #             int(deaths.replace(',', '')),
    #             continent
    #         ))
    #
    #     # StopIteration error is raised when there are no more elements left for iteration
    #     except StopIteration:
    #         break


def main():
    # if HTML file is with your Python code
    # filename = 'HelloWorld.html'
    # webbrowser.open_new_tab(filename)
    # if HTML file is in the working directory (modify for desktop, downloads, etc.)

    # old_code()

    states = scrape_state_data()

    headers = ['States', 'Abbreviation', 'Capital']
    data = [['Alaska', 'Ak', 'Juneau'], ['New York', 'NY', 'Albany']]
    table = create_table(headers, states)
    heading = create_element(TAG_H1, "Justin's United States")

    link_attributes = 'rel = "stylesheet" href = "MyStyle.css"'
    link = create_element(TAG_LINK, '', link_attributes, end_tag=False)

    head = create_element(TAG_HEAD, link)
    body = create_element(TAG_BODY, heading + table) #+ TAG_BR
    message = create_element(TAG_HTML, head + body)

    write_file('states.html', message)
    open_file_in_browser('states.html')


def old_code():
    head = create_element(TAG_HEAD, '')
    p = create_element(TAG_PAR, 'Hello Justin')
    body = create_element(TAG_BODY, p)
    message = TAG_DOCTYPE + create_element(TAG_HTML, head + body)
    write_file('Justin.html', message)
    open_file_in_browser('Justin.html')
    row0 = create_elements(TAG_TH, ['Firstname', 'Lastname', 'Age'])
    row1 = create_elements(TAG_TD, ['Jill', 'Smith', '50'])
    row2 = create_elements(TAG_TD, ['Eve', 'Jackson', '94'])
    rows = create_elements(TAG_TR, [row0, row1, row2])
    table = create_element(TAG_TABLE, rows)
    head = create_element(TAG_HEAD, 'People and their ages')
    heading = create_element(TAG_H1, 'some heading goes here')
    body = create_element(TAG_BODY, heading + table)  # + TAG_BR
    message = create_element(TAG_HTML, head + body)
    write_file('people.html', message)
    open_file_in_browser('people.html')


if __name__ == "__main__":
    main()
