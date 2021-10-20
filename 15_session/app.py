#Team Berd: Austin Ngan (Gerald), Thomas Yu (Perry), Mark Zhu (Bob the Third Jr)
#SoftDev
#K15: Sessions Greetings
#2021-10-19

from flask import Flask             #facilitate flask webserving
from flask import render_template   #facilitate jinja templating
from flask import request           #facilitate form submission
from flask import session           #facilitate session

#the conventional way:
#from flask import Flask, render_template, request

app = Flask(__name__)    #create Flask object

teamBerd = "Team Berd: Austin Ngan, Thomas Yu, Mark Zhu" #TNPG + roster for both landing and response pages
username = "Username"
password = "Password123"


2021-10-14
@app.route("/") #, methods=['GET', 'POST'])
def disp_loginpage():
    '''For the landing page where the user will login with a username'''
    #print("\n\n\n")
    #print("***DIAG: this Flask obj ***")
    #print(app)
    #print("***DIAG: request obj ***")
    #print(request)
    #print("***DIAG: request.args ***") #Prints a dictionary that is empty
    #print(request.args)
    #print("***DIAG: request.args['username']  ***")
    #print(request.args['username'])
    #print("***DIAG: request.headers ***")
    #print(request.headers)
    return render_template( 'login.html' , heading = teamBerd) #Only thing that is added to login page is the heading


@app.route("/auth")#	, methods=['GET', 'POST'])
def authenticate():
    '''The response page that will display a greeting, the username, and the request method used'''
    #print("\n\n\n")
    #print("***DIAG: this Flask obj ***")
    #print(app)
    #print("***DIAG: request obj ***")
    #print(request)
    #print("***DIAG: request.args ***") #Prints a dictionary that now has the username as well as submit.
    #print(request.args)
    #print("***DIAG: request.args['username']  ***")
    #print(request.args['username'])
    #print("***DIAG: request.headers ***")
    #print(request.headers)
    greet = "" #Greeting to be displayed on the response page
    if (request.method == 'GET'): #getting user and pass for GET
        User = request.args['username']
        Pass = request.args['password']
    elif (request.method == 'POST'): #getting user and pass for POST
        User = request.form['username']
        Pass = request.form['password']
    if (User != username): #wrong username
        greet += "Error: Username is incorrect. "
    if (Pass != password): #wrong password
        greet += "Error: Password is incorrect. "
    if (User == username and Pass == password):
        greet += "Hullo humon, Berd appreciates your visit. Enjoy your stay. "
    return render_template('response.html', heading = teamBerd, greeting = greet, username = User, password = Pass, request = request.method)  #uses response template to create the webpage


if __name__ == "__main__": #false if this file imported as module
    #enable debugging, auto-restarting of server when this file is modified
    app.debug = True
    app.run()
