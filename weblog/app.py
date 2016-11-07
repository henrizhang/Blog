from flask import Flask, render_template, request, redirect, url_for, session, Markup
import hashlib, os
from utils.auth import addUser, userLogin 
from utils.display import retStoryID, retTitle, nretTitle, retUpdate, retStory

app=Flask(__name__)
app.secret_key=os.urandom(32)

@app.route("/")
def send():
    if 'userID' in session:
        return redirect(url_for('dispHome'))
    if("msg" in request.args.keys()):
        print "hi"
        return redirect(url_for('dispLogin')+"?msg="+request.args['msg'])
    return redirect(url_for('dispLogin'))

@app.route("/login")
def dispLogin():
    if 'msg' in request.args.keys():
        return render_template("login.html", msg=request.args['msg'])
    return render_template("login.html", msg ="")

@app.route("/auth", methods=['POST'])
def auth():
    if 'register' in request.form.keys():
        msg=addUser(request.form['user'], request.form['pass'])
        print msg
    else:
        info = userLogin(request.form['user'], request.form['pass'])
        if(info[0]=='True'):
            msg=info[1]
            session['userID']=request.form['user']
            print "hi"
        msg=info[1]
    return redirect(url_for('send')+"?msg="+msg)

@app.route("/logout")
def logout():
    session.pop('userID')
    return redirect(url_for('send'))

@app.route("/home")
def dispHome():
    listTitles = retTitle( session[ "userID" ] )
    strTitles = ""
    nlistTitles = nretTitle( session[ "userID" ] )
    nstrTitles = ""
    for title in listTitles:
        strTitles += Markup("<form action=\"/full\" method=\"POST\">")
        strTitles += Markup("<input type=\"submit\" name=\"read\" value=\"" + title[0] + "\">")
        strTitles += Markup("</form>")
        strTitles += Markup("<br>")
    for ntitle in nlistTitles:
        nstrTitles += Markup("<form action=\"/full\" method=\"POST\">")
        nstrTitles += Markup("<input type=\"submit\" name=\"add\" value=\"" + ntitle[0] + "\">")
        nstrTitles += Markup("</form>")
        nstrTitles += Markup("<br>")
    return render_template("home.html",storyTitles=strTitles,nstoryTitles=nstrTitles)

@app.route("/full", methods=["POST"])
def dispFull():
    if "add" in request.form.keys():
        title = request.form["add"]
        content = retUpdate( title )
    else:
        title = request.form["read"]
        content = retStory( title )
    return render_template("add.html",storyTitle=title,storyContent=content)

@app.route("/add", methods=["POST", "GET"])
def addStory():
    return render_template("newStory.html")

if __name__ == "__main__":
    app.debug = True
    app.run()
