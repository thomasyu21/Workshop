#Team Berd: Austin Ngan (Gerald), Thomas Yu (Perry), Mark Zhu (Bob the Third Jr)
#SoftDev
#K15: Sessions Greetings
#2021-10-19

from flask import Flask             #facilitate flask webserving
from flask import render_template   #facilitate jinja templating
from flask import request           #facilitate form submission
from flask import session           #facilitate session
import os                           #to create the secret key

#the conventional way:
#from flask import Flask, render_template, request

app = Flask(__name__)    #create Flask object
app.secret_key = os.urandom(32) #secret key for flask to work

teamBerd = "Team Berd: Austin Ngan, Thomas Yu, Mark Zhu" #TNPG + roster for both landing and response pages
username = "Username"
password = "Password123"

@app.route("/") #, methods=['GET', 'POST'])
def disp_loginpage():
    '''For the landing page where the user will login with a username. If there is already a session, the repsonse page will be generated'''
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
    if 'user' in session: #if there is a user in session takes them to a response page
        greet = "Hullo humon, Berd appreciates your visit. Enjoy your stay. "
        return render_template('response.html', heading = teamBerd, greeting = greet, username = "Username: " + session['user'], request = request.method)
    else:
        return render_template( 'login.html') #If no user in session takes the user to the login page


@app.route("/auth"	, methods=['GET', 'POST'])
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
    try:
        greet = "" #Greeting to be displayed on the response page
        if (request.method == 'GET'): #getting user and pass for GET
            return render_template('login.html', warning = "Please use a POST request")
        elif (request.method == 'POST'): #getting user and pass for POST
            tempUser = request.form['username']
            tempPass = request.form['password']
        if (tempUser != username): #wrong username
            greet += "Error: Username is incorrect. "
        if (tempPass != password): #wrong password
            greet += "Error: Password is incorrect. "
        if (tempUser == username and tempPass == password): #correct username and password
            greet += "Hullo humon, Berd appreciates your visit. Enjoy your stay. "
            session['user'] = tempUser #creates session with username
            return render_template('response.html', heading = teamBerd, greeting = greet, username = "Username: " + tempUser, password = tempPass, request = request.method)  #uses response template to create the webpage
        else:
            return render_template('response.html', heading = teamBerd, greeting = greet, request = request.method)
    except:
        return render_template('login.html', warning = "Something Went Wrong.")

@app.route("/logOut")
def logOut():
    '''For when the user logs out of the session'''
    if 'user' in session: #if user in session remove session and take user back to login page with extra text
        session.pop('user',None)
        return render_template('login.html',warning="You have successfully logged out.")
    else: #no user in session just takes the user back to the login page with no extra text
        return render_template('login.html')

if __name__ == "__main__": #false if this file imported as module
    #enable debugging, auto-restarting of server when this file is modified
    app.debug = True
    app.run()
