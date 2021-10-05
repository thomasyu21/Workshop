# Trio Of Success: Raymond Yeung, Thomas Yu, Annabel Zhang
# K10 -- Flask w/ RandomOccupations
# SoftDev
# 2021-10-04

import random
import csv
from flask import Flask
app = Flask(__name__) 

#@app.route("/")

occupations = {}

with open ('occupations.csv', newline='') as csvfile:
      file = csv.DictReader(csvfile)
      for lines in file:
        occupations[lines['Job Class']] = float(lines['Percentage'])
        
@app.route("/")
def randomOccupations():
    
    ranNum = random.random() * 99.8
    lower = 0
    upper = 0

    for job, percentage in occupations.items():
        lower = upper
        upper += percentage
        if lower <= ranNum < upper:
            #return(job)
            j = job

    #<b> = bold
    #<br> = break (newline)
    occupationstr = "<b>Occupations</b>: <br>"
    
    for x in occupations.keys():
        if x != "Total":
            occupationstr += x + "<br>"

    heading = "Trio Of Success: Raymond Yeung, Thomas Yu, Annabel Zhang <br> K10 -- Flask w/ RandomOccupations <br> SoftDev <br> 2021-10-05 <br><br>"
    
    return(heading + occupationstr + "<br><br> Random Occupation: " + j)
        
app.debug = True
app.run() 
                

