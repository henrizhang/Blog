import csv
import sqlite3

#helper: make a list of the storyIDs that user contributed to
def retStoryID( userID ):
    f="../data/tables.db"
    db=sqlite3.connect(f)
    c=db.cursor()

    q = "SELECT storyID FROM updates WHERE updates.userID = " + str( userID )
    c.execute(q)
    retList = c.fetchall()

    db.commit()
    db.close()

    return retList

#return list of titles that user contributed to
def retTitle( userID ):
    f="../data/tables.db"
    db=sqlite3.connect(f)
    c=db.cursor()

    listStoryID = retStoryID( userID )
    retList = []
    for storyID in listStoryID:
        q = "SELECT title FROM stories WHERE storyID = " + str( storyID )
        c.execute(q)
        appendList = c.fetchall()
        retList = retList + appendList
    
    db.commit()
    db.close()

    return retList

#test cases
print retStoryID( 1 )
print retTitle( 1 )
