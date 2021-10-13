# Team PPS: Kevin Cao (Pipi), Thomas Yu (Perry), Han Zhang(Sirap)
# SoftDev
# K13: Template for Success
# 2021-10-8

from flask import Flask, render_template
import random
import csv


app = Flask(__name__)  # create instance of class Flask

d = {}
with open("data/occupations.csv", mode = 'r') as csvfile:
    file = csv.DictReader(csvfile)
    for lines in file:
        d[lines['Job Class']] = float(lines['Percentage'])

@app.route("/")
def index():
    return "<h1>Home Page</h1>"

@app.route("/occupyflaskst")  # assign fxn to route
def main():
    """ Returns the template webpage using imported csv file in dictionary. """

    return render_template( 'tablified.html', title='K13', heading=heading(), occupations=d, occupation=randomoccupation() )

def heading():
    """returns heading with TNPG + roster"""
    return "Team PPS: Kevin Cao (Pipi), Thomas Yu (Perry), Han Zhang(Sirap)"


def randomoccupation():
    """returns a random occupation with weighted percentage values for csv file"""
    randomNum = random.random()* 99.8

    x = 0.0
    for i, j in d.items():
        if x <= randomNum < x + j:
            return ("Your occupation is: " + i)
            break
        x += j

if __name__ == "__main__":  # true if this file NOT imported
    app.debug = True        # enable auto-reload upon code change
    app.run()
