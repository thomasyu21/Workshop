#Trio of Success: Raymond Yeung, Annabel Zhang, Thomas Yu
#SoftDev
#K06: Random Occupations With Weighted Probability
#2021-09-28

'''
Summary:
 - We used DictReader to read the csv file and then iterated through it
 into a dictionary.
 - We looked at the probabilities of each job by
 iterating through the dictionary and then using a randomly generated
 number between 0 and 99.8.
 - We treated the percentage as the how big the interval between the
 two numbers are.
     - It doesn't matter where the interval is, it just matters the
     size of the interval. If the random number falls in between that
     interval we returned the corresponding job.
'''

import random
import csv

occupations = {}

#DictReader treats the first line of the file as headings for each section (Job Class and Percentage)
#fileheadings = key, everything else in that column of the csv file = value corresponding to key
with open("occupations.csv", newline='') as csvfile:
    file = csv.DictReader(csvfile)
    #adding jobs and percentages as key:value pairs to the dictionary
    for lines in file:
        occupations[lines['Job Class']] = float(lines['Percentage'])

#generate a random number from 0 inclusive to 99.8 exclusive
ranNum = random.random() * 99.8
#variables to limit the interval for each job
lower = 0
upper = 0

#loop through the dictionary
for job, percentage in occupations.items():
    #set the interval = previous upper bound to upper bound + percentage
    #percentage = size of interval -> weighted probability
    lower = upper
    upper += percentage
    #check if ranNum is within the interval and if so print the job
    if lower <= ranNum < upper:
        print(job)
    
