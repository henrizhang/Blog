import csv
import sqlite3

def addToDb(story, update, username):
	f="../data/tables.db"
    db=sqlite3.connect(f)
    c=db.cursor()
	q = "INSERT INTO updates VALUES (username)"
	c.execute(q)
	q = "UPDATE table_name SET recent=update WHERE storyId=story"
	c.execute(q)

def addNewStory(content, username):
	f="../data/tables.db"
    db=sqlite3.connect(f)
    c=db.cursor()
    q="INSERT INTO stories VALUES (userID, content, content)"