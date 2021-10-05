# Trio Of Success: Raymond Yeung, Thomas Yu, Annabel Zhang
# K10 -- Flask Testing
# SoftDev
# 2021-10-04

from flask import Flask
app = Flask(__name__) # Q0: Where have you seen similar syntax in other langs?

@app.route("/") # Q1: What points of reference do you have for meaning of '/'?
def hello_world():
    print(__name__) # Q2: Where will this print to? Q3: What will it print?
    return "No hablo queso!"  # Q3: Will this appear anywhere? How u know?

app.run()  # Q4: Where have you seen similar construcs in other languages?
                
#This is the same as the assignment from K09
#app.run() runs the entire program
#In the terminal on the school machines, "__main__" is printed when the website is accessed
#On my home machine (Windows), "__main__" is printed after I quit
