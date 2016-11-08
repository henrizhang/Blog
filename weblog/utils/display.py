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

def nretStoryID( username ):
    f="data/tables.db"
    db=sqlite3.connect(f)
    c=db.cursor()

    listStoryID = retStoryID( username )
    retList = []

    q = "SELECT storyID FROM stories;"
    c.execute(q)
    fullList = c.fetchall()
    newList = []
    for storyID1 in fullList:
        check = False
        for storyID2 in listStoryID:
            if storyID1[0] == storyID2[0]:
                check = True
                break
        if not check:
            newList.append( storyID1[0] )

    db.commit()
    db.close()
    
    return newList

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

    q = "SELECT storyID FROM stories;"
    c.execute(q)
    fullList = c.fetchall()
    newList = []
    for storyID1 in fullList:
        check = False
        for storyID2 in listStoryID:
            if storyID1[0] == storyID2[0]:
                check = True
                break
        if not check:
            newList.append( storyID1[0] )

    for storyID in newList:
        q = "SELECT title FROM stories WHERE storyID = " + str( storyID ) + ";"
        c.execute(q)
        appendList = c.fetchall()
        retList = retList + appendList

    db.commit()
    db.close()

    return retList

def retUpdate( storyID ):
    f="data/tables.db"
    db=sqlite3.connect(f)
    c=db.cursor()

    q = "SELECT lastUpdate FROM stories WHERE storyID = " + str(storyID) + ";"
    c.execute(q)
    update = c.fetchall()[0][0]
    print update
    
    q = "SELECT updateContent FROM updates WHERE storyID = " + str(storyID) + " AND updateNum = " + str(update) + ";"
    c.execute(q)
    retVal = c.fetchall()[0][0]

    db.commit()
    db.close()
    
    return retVal


def retStory( storyID ):
    f="data/tables.db"
    db=sqlite3.connect(f)
    c=db.cursor()

    q = "SELECT content FROM stories WHERE storyID = " + str(storyID) + ";"
    c.execute(q)
    if len(c.fetchall())<1:
        return "error"
    if len(c.fetchall()[0])<1:
        return "error"
    retVal = c.fetchall()

    db.commit()
    db.close()

    return retVal[0][0]

#test cases
print retUpdate( 1 )
