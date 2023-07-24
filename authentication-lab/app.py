from flask import Flask, render_template, request, redirect, url_for, flash
from flask import session as login_session
import pyrebase
config = {
  "apiKey": "AIzaSyBzRPe_OMQQU3NNdHMeH7fNUlQl17CKz9k",
  "authDomain": "aloha-d6953.firebaseapp.com",
  "projectId": "aloha-d6953",
  "storageBucket": "aloha-d6953.appspot.com",
  "messagingSenderId": "356364790039",
  "appId": "1:356364790039:web:d0351f44a45368361eaf52",
  "measurementId": "G-CQRZT8NKQ1",
    "databaseURL": ""
}
app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['SECRET_KEY'] = 'super-secret-key'

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
@app.route('/', methods=['GET', 'POST'])
def signin():
    return render_template("signin.html")


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        return render_template("signup.html")
        email = request.form["email"]
        password = request.form["password"]
        try:
            login_session['user'] = auth.create_user_with_email_and_password(email, password)
            return redirect(url_for('signin'))
        except:
            return('epic fail')


@app.route('/add_tweet', methods=['GET', 'POST'])
def add_tweet():
    return render_template("add_tweet.html")




if __name__ == '__main__':
    app.run(debug=True)