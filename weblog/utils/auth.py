import hashlib, sqlite3


def addUser(user, password):
    db=sqlite3.connect('../data/tables.db')
    c=db.cursor()
    myHashObj=hashlib.sha1()
    myHashObj.update(password)
    q='SELECT username FROM users'
    if(user in c.execute(q)):
        return False
    q='SELECT userID FROM users'
    q='INSERT INTO users ('+str(c.execute(q)[len(c.execute(q))-1]+1)+', '+user+', '+myHashObj.hexdigest()+');'
    c.execute(q)
    return True

def userLogin(user, password)
    db=sqlite3.connect('../data/tables.db')
    c=db.cursor()
    myHashObj=hashlib.sha1()
    myHashObj.update(password)
    q='SELECT username FROM users'
    if(user in c.execute(q)):
        q='SELECT pass FROM users WITH username='+user+';'
