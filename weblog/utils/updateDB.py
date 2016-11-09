import csv
import sqlite3


def updateStory(storyID, updateCon, userID):
	print storyID
	print "wtf"
	updateCon=updateCon+"\n"
	f="data/tables.db"
	db=sqlite3.connect(f)
	c=db.cursor()
	q="SELECT userID from users where username=\""+userID+"\""
	c.execute(q)
	userID=c.fetchall()[0][0]
	#fixing userID disrepancy

	q="SELECT lastUpdate from stories where storyID=\""+str(storyID)+"\";"
	q=c.execute(q)
	latestUpdateNumber=c.fetchall()[0][0]
    #fetching the latest updateNum of the story to know what updateNum of the new one will be
	latestUpdateNumber+=1

	q = "INSERT INTO updates VALUES (\""+str(latestUpdateNumber)+"\", "+str(storyID)+", \""+str(userID)+"\", \""+updateCon+"\");"
	c.execute(q)
	#adding 'updates' record

	q = "UPDATE stories SET lastUpdate=\""+str(latestUpdateNumber)+"\" WHERE storyID="+str(storyID)+";"
	c.execute(q)

	q="SELECT content from stories where storyID=\""+str(storyID)+"\";"
	q=c.execute(q)
	oldContent=c.fetchall()[0][0]
	q = "UPDATE stories SET content=\""+oldContent+updateCon+"\" WHERE storyID="+str(storyID)+";"
	c.execute(q)
	db.commit()



	#updating the stories record to reflect the latest change


def addNewStory(content, username, title):
	f="data/tables.db"
	db=sqlite3.connect(f)
	c=db.cursor()
	q="SELECT userID from users where username=\""+username+"\""
	c.execute(q)
	userID=c.fetchall()[0][0]
	q="INSERT INTO stories VALUES (NULL,\""+ content+"\",\""+ title+"\", 1);"
	c.execute(q)
	print content
	print "this is content"
	print title
	print "this is title"
	q="SELECT storyID from stories where content=\""+content+"\";"
	q=c.execute(q)
	storyID=c.fetchall()
	finalID=0
	for x in storyID:
		finalID+=int(x[0])
	q="INSERT INTO updates VALUES (1,"+str(finalID)+", \""+str(userID)+"\", \""+content+"\");"
	c.execute(q)
	db.commit()
