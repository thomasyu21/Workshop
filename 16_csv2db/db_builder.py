#Team Berd: Austin Ngan (Gerald), Thomas Yu (Perry), Mark Zhu (Bob the Third Jr)
#SoftDev
#K16: All About Database
#2021-10-24

import sqlite3   #enable control of an sqlite database
import csv       #facilitate CSV I/O


DB_FILE="discobandit.db"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops -- you will use cursor to trigger db events

#==========================================================

'''adds name, age, and id to the corresponding parts of the roster table'''
c.execute("CREATE TABLE IF NOT EXISTS roster (name TEXT, age INTEGER, id INTEGER)") #creates the table
with open("students.csv", newline='') as csvfile: #reads in the csv file
    studentReader = csv.DictReader(csvfile)
    for row in studentReader:
        c.execute("INSERT INTO roster VALUES (?, ?, ?)", (f"{row['name']}", row['age'], row['id'])) #adds each row of the csv file into the db

'''adds code, mark, and id to the corresponding parts of the courses table'''
c.execute("CREATE TABLE IF NOT EXISTS courses (code TEXT, mark INTEGER, id INTEGER)") #creates table
with open("courses.csv", newline='') as csvfile: #reads in csv file
    coursesReader = csv.DictReader(csvfile)
    for row in coursesReader:
        c.execute("INSERT INTO courses VALUES (?, ?, ?)", (f"{row['code']}", row['mark'], row['id'])) #adds each row of the csv file into the db

#command = ""          # test SQL stmt in sqlite3 shell, save as string
#c.execute(command)    # run SQL statement

#==========================================================

db.commit() #save changes
db.close()  #close database
