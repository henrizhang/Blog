import csv
import sqlite3

f="../data/tables.db"
db=sqlite3.connect(f)
c=db.cursor()

#make a list of the storyIDs in updates that the user contributed to
q = "SELECT storyID FROM updates WHERE updates.userID = " + 
