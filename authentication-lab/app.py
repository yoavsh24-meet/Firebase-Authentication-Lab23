from flask import Flask, render_template, request, redirect, url_for, flash
from flask import session as login_session
import pyrebase

app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['SECRET_KEY'] = 'super-secret-key'

config = {
  "apiKey": "AIzaSyDczgJfyL9axKQ2-nbeMDPdeie4aiqWW9Y",
  "authDomain": "hungerforflesh-5b423.firebaseapp.com",
  "projectId": "hungerforflesh-5b423",
  "storageBucket": "hungerforflesh-5b423.appspot.com",
  "messagingSenderId": "647572238228",
  "appId": "1:647572238228:web:49987a13db03d38751e981","databaseURL": ""

};
@app.route('/', methods=['GET', 'POST'])
def signin():
    return render_template("signin.html")


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    return render_template("signup.html")


@app.route('/add_tweet', methods=['GET', 'POST'])
def add_tweet():
    return render_template("add_tweet.html")
firebase = pyrebase.initialize_app(config)
auth = firebase.auth()

app = Flask(__name__, template_folder='templates', static_folder='static')


if __name__ == '__main__':
    app.run(debug=True)