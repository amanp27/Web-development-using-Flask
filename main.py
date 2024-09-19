from flask import Flask, render_template, request, redirect
from db import Database

app = Flask(__name__)
dbo = Database()


@app.route('/')
def index():
    return render_template('login.html')


@app.route('/register')
def register():
    return render_template('register.html')


@app.route('/perform_registration', methods=['post'])
def perform_registration():
    name = request.form.get('user_name')
    email = request.form.get('user_email')
    password = request.form.get('user_password')

    response = dbo.insert(name, email, password)

    if response:
        return render_template('login.html', message="Login Successful, Kindly Login to proceed")
    else:
        return render_template("register.html", message="Email Already Exist")


@app.route("/perform_login", methods=['post'])
def perform_login():
    email = request.form.get('user_email')
    password = request.form.get('user_password')

    response = dbo.search(email, password)

    if response:
        return redirect('/profile')
    else:
        return render_template('login.html', message = 'Incorrect Email/Password')

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/ner')
def ner():
    return render_template('ner.html')

@app.route('/perform_ner', methods = ['post'])
def perform_ner():
    return "NER is Working, API NOT FOUND"

@app.route('/sentiment_analysis')
def sentiment_analysis():
    return render_template("sentiment_analysis.html")

#@app.route('/perform_sentiment')
#def perform_sentiment():
#    return "Code In Progress"

@app.route('/abuse_detection')
def abuse_detection():
    return render_template('abuse_detection.html')

app.run(debug=True)
