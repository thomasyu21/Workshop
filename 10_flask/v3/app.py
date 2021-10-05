# Trio Of Success: Raymond Yeung, Thomas Yu, Annabel Zhang
# K10 -- Flask Testing
# SoftDev
# 2021-10-04

from flask import Flask
app = Flask(__name__) #create instance of class Flask

@app.route("/")       #assign fxn to route
def hello_world():
    print("about to print __name__...")
    print(__name__)   #where will this go?
    return "No hablo queso!"

app.debug = True #What does debugger mode allow the user to do with in the terminal and on the web page?
#Big block of text should say debugger = true
app.run()

#A Debugger Pin is provided -> What is this used for?
