# Trio Of Success: Raymond Yeung, Thomas Yu, Annabel Zhang
# K10 -- Flask Testing
# SoftDev
# 2021-10-04

from flask import Flask
app = Flask(__name__) #create instance of class Flask

@app.route("/")       #assign fxn to route
def hello_world():
    print("about to print __name__...") #This is an extra print statement
    print(__name__)   #Should print to the terminal on the same line as the previous print statement
    return "No hablo queso!"

app.run()

#The two print statements did not print on the same line.
