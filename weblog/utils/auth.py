import hashlib, sqlite3


def addUser(user, password):
    db=sqlite3.connect('data/tables.db')
    c=db.cursor()
    myHashObj=hashlib.sha1()
    myHashObj.update(password)
    q='SELECT * FROM users'
    c.execute(q)
    userInfo=c.fetchall()
    for data in userInfo:
        if (user in data):
            db.close()
            return "ERROR: username already in use"
    q='INSERT INTO users VALUES ("'+str(userInfo[len(userInfo)-1][0]+1)+'", "'+user+'", "'+myHashObj.hexdigest()+'")'
    print q
    c.execute(q)
    db.commit()
    db.close()
    return "registration succesful, enter user and pass to login"

def userLogin(user, password):
    db=sqlite3.connect('data/tables.db')
    c=db.cursor()
    myHashObj=hashlib.sha1()
    myHashObj.update(password)
    q='SELECT username FROM users'
    print "hi"
    c.execute(q)
    data=c.fetchall()
    for stuff in data:
        if(user in stuff):
            print "bye"
            q='SELECT password FROM users WHERE username = "'+user+'";'
            c.execute(q)
            password=c.fetchall()
            db.close()
            if(myHashObj.hexdigest()==password[0][0]):
                return True
    db.close()
    return False
