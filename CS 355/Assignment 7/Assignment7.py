from flask import Flask, render_template, request, redirect, url_for, session
import pymysql
import hashlib
import re

app = Flask(__name__)
app.secret_key = 'your secret key'


def connect_to_mars():
    password = read_password()
    conn = pymysql.connect(host="mars.cs.qc.cuny.edu", port=3306, user="daju9399", passwd=password, database="daju9399")
    return conn


@app.route('/states')
def show_states():
    if not session['loggedin']:
        return 'you are not logged in'
    query = "SELECT * FROM states ORDER BY state_name"
    conn = connect_to_mars()
    cursor = conn.cursor()
    cursor.execute(query)
    states = cursor.fetchall()

    conn.commit()
    conn.close()
    headers = ['Abbreviation', 'Name', 'Capital']
    return render_template('states.html', headers=headers, data=states)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


@app.route('/success/<name>')
def success(name):
    return 'welcome %s' % name


@app.route('/hello/<name>')
def hello_name(name):
    return 'hello %s!' % name


def read_password():
    with open("password.txt") as file:
        password = file.read().strip()
    return password


@app.route('/login', methods=['POST', 'GET'])
def login():
    msg = ''
    if request.method == 'POST' and 'login' in request.form and 'password' in request.form:
        conn = connect_to_mars()
        cursor = conn.cursor()
        typed_login = request.form['login']
        typed_password = request.form['password']
        md5_password = hashlib.md5(typed_password.encode('utf-8')).hexdigest()
        query = "SELECT user_id FROM app_user WHERE login = '" + typed_login + "' AND pwd = '" + md5_password + "'"
        # print(query)
        cursor.execute(query)
        user_row = cursor.fetchone()
        # print(user_row)
        if user_row:
            session['loggedin'] = True
            session['id'] = user_row[0]
            # print(session['id'])
            msg = 'Logged in successfully !'
            # print(msg)
            return render_template('index.html', msg=msg)
        else:
            msg = 'Incorrect username / password !'
    return render_template('login.html', msg=msg)


@app.route('/logout')
def logout():
    session.pop('loggedin', None)
    session.pop('id', None)
    return redirect(url_for('login'))


@app.route('/register', methods =['GET', 'POST'])
def register():
    msg = ''
    if request.method == 'POST' and 'login' in request.form and 'password' in request.form and \
            'email' in request.form and 'fname' in request.form and 'lname' in request.form:
        first_name = request.form['fname']
        last_name = request.form['lname']
        typed_login = request.form['login']
        typed_password = request.form['password']
        typed_email = request.form['email']
        conn = connect_to_mars()
        cursor = conn.cursor()
        md5_password = hashlib.md5(typed_password.encode('utf-8')).hexdigest()
        query = "SELECT login FROM app_user WHERE login = '" + typed_login + "' AND pwd = '" + md5_password + "'"
        # print(query)
        cursor.execute(query)
        user_row = cursor.fetchone()
        if user_row:
            msg = 'Account already exists !'
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', typed_email):
            msg = 'Invalid email address !'
        elif not re.match(r'[A-Za-z]+', typed_login):
            msg = 'name must contain only characters!'
        else:
            cursor.execute('INSERT INTO app_user VALUES (NULL, % s, % s, % s, % s, % s)',
                           (first_name, last_name, typed_login, md5_password, typed_email))
            conn.commit()
            msg = 'You have successfully registered !'
    elif request.method == 'POST':
        msg = 'Please fill out the form !'
    return render_template('register.html', msg=msg)


@app.route("/index")
def index():
    if 'loggedin' in session:
        return render_template("index.html")
    return redirect(url_for('login'))


@app.route("/display")
def display():
    if 'loggedin' in session:
        conn = connect_to_mars()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM app_user WHERE user_id = % s', session['id'])
        user_row = cursor.fetchall()
        print(user_row)
        return render_template("display.html",  user_row=user_row[0])
    return redirect(url_for('login'))


@app.route("/update", methods=['GET', 'POST'])
def update():
    msg = ''
    if 'loggedin' in session:
        if request.method == 'POST' and 'login' in request.form and 'password' in request.form and\
                'email' in request.form and 'fname' in request.form and 'lname' in request.form:
            first_name = request.form['fname']
            last_name = request.form['lname']
            typed_login = request.form['login']
            typed_password = request.form['password']
            typed_email = request.form['email']
            conn = connect_to_mars()
            cursor = conn.cursor()
            md5_password = hashlib.md5(typed_password.encode('utf-8')).hexdigest()
            query = "SELECT login FROM app_user WHERE login = '" + typed_login + "' AND pwd = '" + md5_password + "'"
            # print(query)
            cursor.execute(query)
            user_row = cursor.fetchone()
            # print(user_row)
            if user_row:
                msg = 'Account already exists !'
            elif not re.match(r'[^@]+@[^@]+\.[^@]+', typed_email):
                msg = 'Invalid email address !'
            elif not re.match(r'[A-Za-z]+', typed_login):
                msg = 'name must contain only characters!'
            else:
                # print(session['id'])
                cursor.execute('UPDATE app_user SET  first_name =% s, last_name =% s, login =% s, pwd =% s,'
                               ' email =% s WHERE user_id =% s',
                               (first_name, last_name, typed_login, md5_password, typed_email, session['id']))
                conn.commit()
                msg = 'You have successfully updated !'
        elif request.method == 'POST':
            msg = 'Please fill out the form !'
        return render_template("update.html", msg=msg)
    return redirect(url_for('login'))


if __name__ == '__main__':
    app.run()