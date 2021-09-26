#Thomas Yu
#SoftDev
#Print A SoftDev Student's Name
#2021-9-21

import random

#global variables
pd1 = []
pd2 = []

#takes in a period number input and prints a random "student's" name
def printName():
    global pd1, pd2
    period = int(input("Search!\nPeriod Number: "))
    
    if period == 1:
        check(pd1, 'pd1.txt')
        
    elif period == 2:
        check(pd2, 'pd2.txt')
        
    else:
        print("This is not a valid period.")

#reads in the corresponding list and txt file, and adds to it
#throws error responses if there is no file or if file is empty
def check(list, txt):
    global pd1, pd2
    try:
        with open(txt, 'r') as file:
            for line in file:
                line = line.rstrip('/n')
                list.append(line)
        try:
            rand = random.randint(0, len(list) - 1)
            print(list[rand])
        except:
            print("Text file is empty")
    except:
        print("There is no such file")

printName()
