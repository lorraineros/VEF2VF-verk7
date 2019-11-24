import os
from flask import Flask, flash, redirect, render_template, request, url_for, make_response, escape, session, abort
from pymysql import *

app = Flask(__name__)

app.secret_key = os.urandom(16)   
print(os.urandom(16))

connection = connect(host='tsuts.tskoli.is', port=3306, user='2509022390', password='mypassword', database='2509022390_vef2_v7', autocommit=True)

@app.route("/")
def index():
    with connection.cursor() as cursor:
        cursor.execute("select * from 2509022390_vef2_v7.users")
        users = cursor.fetchall()

    if 'user' in session:
        user = session['user']
    else: 
        user = {"name":"none", "password":"none", "email":"none"}

    return render_template('main.tpl', user=user)


@app.route("/innskraning", methods=['GET', 'POST'])
def innskraning():
    error = False
    if 'user' in session:
        return redirect(url_for('index'))

    with connection.cursor() as cursor:
        cursor.execute("select * from 2509022390_vef2_v7.users")
        users = cursor.fetchall()

    if request.method == 'POST':
        error = True
        for u in users:
            if request.form['name'] == u[0]:
                if request.form['password'] == u[1]:
                    session['user'] = {"name":u[0], "password":u[1], "email":u[2]}
                    return redirect(url_for('index'))
    return render_template('login.tpl', error=error)

@app.route('/sida')
def sida():
    if 'user' in session:
        user = session['user']
    else:
        return redirect(url_for('innskraning'))

    return render_template('sida.tpl', user=user)

@app.route('/utskraning')
def utskraning():
    if 'user' in session:
        session.pop('user')
    return redirect(url_for('index'))

@app.route('/nyrnotandi', methods=['GET', 'POST'])
def nyrnotandi():
    error = False
    if 'user' in session:
        return redirect(url_for('index'))

    with connection.cursor() as cursor:
        cursor.execute("select * from 2509022390_vef2_v7.users")
        users = cursor.fetchall()

    if request.method == 'POST':
        for u in users:
            if u[0] == request.form['name']:
                return render_template('nyrnotandi.tpl', error=True)

        with connection.cursor() as cursor:
            cursor.execute("INSERT INTO 2509022390_vef2_v7.users(name, email, password) VALUES(%s, %s, %s)",(name, email, password))
        return redirect(url_for('innskraning'))

    return render_template('nyrnotandi.tpl', error=error)



@app.errorhandler(404)
def not_found(error):
    return render_template("not_found.tpl"),404

@app.errorhandler(405)
def not_allowed(error):
    return render_template("not_allowed.tpl"),405

if __name__ == '__main__':
    app.run(debug=True)