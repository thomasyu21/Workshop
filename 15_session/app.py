#Team Berd: Austin Ngan (Gerald), Thomas Yu (Perry), Mark Zhu (Bob the Third Jr)
#SoftDev
#K14: Form and Function
#2021-10-14

from flask import Flask             #facilitate flask webserving
from flask import render_template   #facilitate jinja templating
from flask import request           #facilitate form submission

#the conventional way:
#from flask import Flask, render_template, request

app = Flask(__name__)    #create Flask object

teamBerd = "Team Berd: Austin Ngan, Thomas Yu, Mark Zhu" #TNPG + roster for both landing and response pages
greet = "Hullo humon, Berd appreciates your visit. Enjoy your stay." #Greeting to be displayed on the response page
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
    #print("***DIAG: request.args ***")#Prints a dictionary that now has the username as well as submit.
    #print(request.args)
    #print("***DIAG: request.args['username']  ***")
    #print(request.args['username'])
    #print("***DIAG: request.headers ***")
    #print(request.headers)
    if (request.method) == 'GET':
    	#if (request.args['username']==username and request.args['password']==password):
    	#if (request.args['username']!=username):
    	#if (request.args['password']!=password):

    	return render_template('response.html', heading = teamBerd, greeting = greet, username 		= request.args['username'], request = request.method)  #uses response template to 		create the webpage
    if (request.method) == 'POST':
    	return render_template('response.html', heading = teamBerd, greeting = greet, username 		= request.form['username'], request = request.method)  #uses response template to 		create the webpage


if __name__ == "__main__": #false if this file imported as module
    #enable debugging, auto-restarting of server when this file is modified
    app.debug = True
    app.run()
