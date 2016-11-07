import csv
import sqlite3

def updateStory(story, updateCon, userID):
	f="data/tables.db"
	db=sqlite3.connect(f)
	c=db.cursor()

	latestUpdateNumber="SELECT lastUpdate from stories where storyID=story"
	latestUpdateNumber=c.execute(latestUpdateNumber)
    #fetching the latest updateNum of the story to know what updateNum the new one will be
	latestUpdateNumber+=1
	q = "INSERT INTO updates VALUES (latestUpdateNumber, story, userID, updateCon)"
	c.execute(q)
	#adding 'updates' record
	q = "UPDATE stories SET lastUpdate=updateCon WHERE storyID=story"
	c.execute(q)

	oldContent="SELECT content from stories where storyID=story"
	oldContent=c.execute(oldContent)

	q = "UPDATE stories SET content=oldContent+updateCon WHERE storyID=story"
	c.execute(q)


	#updating the stories record to reflect the latest change


def addNewStory(content, userID, title):
	f="data/tables.db"
	db=sqlite3.connect(f)
	c=db.cursor()
	q="INSERT INTO stories VALUES (1,\""+ content+"\",\""+ title+"\", 1)"
	c.execute(q)
	print "LMAO IM WEAK"
	q="SELECT storyID from stories where content=\""+content+"\""
	q=c.execute(q)
	storyID=c.fetchall()
	finalID=0
	for x in storyID:
		finalID+=1
	q="INSERT INTO updates VALUES (1,"+str(finalID)+", \""+userID+"\", \""+content+"\")"
	c.execute(q)
