# Team dinoClock: Yaying Liang Li, Thomas Yu
# SoftDev
# K19 -- A RESTful Joruney Skyward
# 2021-11-23

from flask import Flask, render_template
import urllib
import json

app = Flask(__name__)

@app.route("/")
def rest_demo():
    uResp = urllib.request.urlopen("https://api.nasa.gov/planetary/apod?api_key=qsb4nvuGri4tJe3q6REknzJbP5xO1OZnJBDfLKMG")#HTTP Response object (containing the JSON info)
    #print(uResp)

    output = json.load(uResp) #load turns the json into a python dictionary.
    #print(output)

    url = output['url'] #value of the 'url' key
    #print(url)

    explanation = output['explanation'] #value of the 'explanation' key
    #print(explanation)

    #render template with image and explanation
    return render_template("main.html", pic = url, description = explanation)

if __name__ == "__main__":
    app.debug = True
    app.run()
