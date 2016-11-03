from flask import Flask, render_template, request, redirect, url_for, session
import hashlib, os
from utils.auth import addUser, userLogin 

app=Flask(__name__)
app.secret_key=os.urandom(32)

@app.route("/")
def send():
    if 'user' in session:
        return redirect(url_for('dispHome'))
    if("msg" in request.args.keys()):
        print "hi"
        return redirect(url_for('dispLogin')+"?msg="+request.args['msg'])
    return redirect(url_for('dispLogin'))

@app.route("/login")
def dispLogin():
    return render_template("login.html", msg=request.args['msg'])

@app.route("/auth", methods=['POST'])
def auth():
    if 'register' in request.form.keys():
        msg=addUser(request.form['user'], request.form['pass'])
        print msg
    elif(userLogin(request.form['user'], request.form['pass'])):
        session['user']=request.form['user']
    return redirect(url_for('send')+"?msg=bad user/pass")

@app.route("/logout")
def logout():
    session.pop('user')
    return redirect(url_for('send'))

@app.route("/home")
def dispHome():
    return 'hi'

if __name__ == "__main__":
    app.debug = True
    app.run()
