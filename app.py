'''
Joyce Wu
Softdev1 pd07
HW13-- A RESTful Journey Skyward
2017-11-09
'''

from flask import Flask, render_template, request
import urllib2
import json

app = Flask(__name__)
uResp = urllib2.urlopen('https://api.nasa.gov/planetary/apod?api_key=5jBJMJZ60Fr5UQYT0C2tWMiqYaGwbFSmZtBXVtin')
info = uResp.read()
d = json.loads(info)

@app.route("/")
def hello():
    title = d["title"]
    copy = d["copyright"]
    date = d["date"]
    image = d["hdurl"]
    explan = d["explanation"]
    return render_template("base.html", title=title, copy=copy, date=date, image=image, explan=explan)

if __name__ == "__main__":
    app.debug = True
    app.run()
