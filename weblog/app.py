from flask import Flask, render_template, request, redirect, url_for, session, Markup
import hashlib, os
from utils.auth import addUser, userLogin
from utils.display import retStoryID, nretStoryID, retTitle, nretTitle, retUpdate, retStory
from utils.updateDB import updateStory,addNewStory

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
    if 'userID' in session:
        return render_template('alreadyLogged.html', msg=session['userID'])
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
    listStoryID = retStoryID( session[ "userID" ] )
    strTitles = ""
    nlistTitles = nretTitle( session[ "userID" ] )
    nlistStoryID = nretStoryID( session[ "userID" ] )
    nstrTitles = ""
    index = 0
    for title in listTitles:
        strTitles += Markup("<form action=\"/full\" method=\"POST\">")
        strTitles += Markup("<input type=\"hidden\" name=\"read\" value=" + str(listStoryID[index][0]) + ">")
        strTitles += Markup("<input type=\"submit\" name=\"submit\" value=\"" + title[0] + "\">")
        strTitles += Markup("</form>")
        strTitles += Markup("<br>")
        index += 1
    index = 0
    for ntitle in nlistTitles:
        nstrTitles += Markup("<form action=\"/full\" method=\"POST\">")
        nstrTitles += Markup("<input type=\"hidden\" name=\"add\" value=" + str(nlistStoryID[index]) + ">")
        nstrTitles += Markup("<input type=\"submit\" name=\"submit\" value=\"" + ntitle[0] + "\">")
        nstrTitles += Markup("</form>")
        nstrTitles += Markup("<br>")
        index += 1
    return render_template("home.html",storyTitles=strTitles,nstoryTitles=nstrTitles)

@app.route("/full", methods=["POST"])
def dispFull():
    if "add" in request.form.keys():
        id = request.form["add"]
        content = retUpdate( id )
        title = request.form["submit"]
    else:
        id = request.form["read"]
        content = retStory( id )
        title = request.form["submit"]
    return render_template("add.html",storyTitle=title,storyContent=content)


@app.route("/add", methods=["POST", "GET"])
def addStory():
    if "title" in request.form.keys() and "content" in request.form.keys():
        addNewStory(request.form["content"],session['userID'],request.form["title"])
        return render_template("home.html")
    return render_template("newStory.html")

@app.route("/update", methods=["POST", "GET"])
def update():
    updateStory(request.form["content"], request.form["update"], session['userID'])
    print "bet"
    return redirect(url_for('dispHome'))



if __name__ == "__main__":
    app.debug = True
    app.run()
