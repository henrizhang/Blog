import csv
import sqlite3

#helper: make a list of the storyIDs that user contributed to
def retStoryID( username ):
    f="data/tables.db"
    db=sqlite3.connect(f)
    c=db.cursor()

    q = "SELECT userID FROM users WHERE username = \"" + username + "\";"
    c.execute(q)
    userID = c.fetchall()
    
    q = "SELECT storyID FROM updates WHERE updates.userID = " + str( userID[0][0] ) + ";"
    c.execute(q)
    retList = c.fetchall()

    db.commit()
    db.close()

    return retList

#return list of titles that user contributed to
def retTitle( username ):
    f="data/tables.db"
    db=sqlite3.connect(f)
    c=db.cursor()

    listStoryID = retStoryID( username )
    retList = []
    for storyID in listStoryID:
        q = "SELECT title FROM stories WHERE storyID = " + str( storyID[0] ) + ";"
        c.execute(q)
        appendList = c.fetchall()
        retList = retList + appendList
    
    db.commit()
    db.close()

    return retList

#return list of titles that user has not contributed to
def nretTitle( username ):
    f="data/tables.db"
    db=sqlite3.connect(f)
    c=db.cursor()

    listStoryID = retStoryID( username )
    retList = []
    for storyID in listStoryID:
        q = "SELECT title FROM stories WHERE storyID != " + str( storyID[0] ) + ";"
        c.execute(q)
        appendList = c.fetchall()
        retList = retList + appendList

    db.commit()
    db.close()

    return retList

#test cases
print retStoryID( "vincent" )
print retTitle( "vincent" )
