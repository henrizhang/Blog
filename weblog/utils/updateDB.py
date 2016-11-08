import csv
import sqlite3

def updateStory(content, updateCon, userID):
	f="data/tables.db"
	db=sqlite3.connect(f)
	c=db.cursor()
	q="SELECT storyID from stories where content=\""+content+"\";"
	print q
	c.execute(q)
	storyID=c.fetchall()
	print storyID
	finalID=0
	for x in storyID:
		finalID+=x
	print finalID
	q="SELECT lastUpdate from stories where storyID=\""+str(finalID)+"\";"
	print q
	q=c.execute(q)
	latestUpdateNumber=c.fetchall()
	print latestUpdateNumber
    #fetching the latest updateNum of the story to know what updateNum the new one will be
	latestUpdateNumber+=1
	q = "INSERT INTO updates VALUES (\""+str(latestUpdateNumber)+"\", "+str(finalID)+", \""+userID+"\", \""+updateCon+"\");"
	print q
	c.execute(q)
	#adding 'updates' record
	q = "UPDATE stories SET lastUpdate=\""+updateCon+"\" WHERE storyID="+str(finalID)+";"
	c.execute(q)

	q="SELECT content from stories where storyID=\""+str(finalID)+"\";"
	print q
	q=c.execute(q)
	oldContentL=c.fetchall()
	oldContent=""
	for x in oldContentL:
		oldContent+=x
	q = "UPDATE stories SET content=\""+oldContent+updateCon+"\" WHERE storyID="+str(finalID)+";"
	print q
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
	print "LMAO IM WEAK"
	q="SELECT storyID from stories where content=\""+content+"\";"
	q=c.execute(q)
	storyID=c.fetchall()
	finalID=0
	for x in storyID:
		finalID+=int(x[0])
	q="INSERT INTO updates VALUES (1,"+str(finalID)+", \""+str(userID)+"\", \""+content+"\");"
	c.execute(q)
	db.commit()
