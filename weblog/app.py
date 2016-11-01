from flask import Flask, render_template, request, redirect, url_for, session
import hashlib, os, util

app=Flask(__name__)
app.secret_key=os.urandom(32)

@app.route("/")
def send():
    if 'username' in session:
        return redirect(url_for('dispHome'))
    return redirect(url_for('auth'))

@app.route("/login", methods=['POST'])
def auth():
    if 'register' in request.form.keys():
        addUser(request.form['user'], request.form['pass'])
    elif(login(request.form['user'], request.form['pass'])):
        session['user']=request.form['user']
    return redirect(url_for('send'))

@app.route("/logout")
def logout():
    session.pop('user')
    return redirect(url_for('send'))

@app.route("/home")
def dispHome():

@app.route("/story")
def dispStory():
    
@app.route("/newstory")
def crtStory():

if __name__ == "__main__":
    app.debug = True
    app.run()
