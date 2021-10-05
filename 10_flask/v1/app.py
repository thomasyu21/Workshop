# Trio Of Success: Raymond Yeung, Thomas Yu, Annabel Zhang
# K10 -- Flask Testing
# SoftDev
# 2021-10-04

from flask import Flask
app = Flask(__name__) #create instance of class Flask

@app.route("/")       #assign fxn to route
def hello_world():
    #print(__name__) not here anymore -> won't print __main__ to the terminal
    return "No hablo queso!"

app.run()
#Should do the same thing on the website

#Same as v0, but missing the print statement
