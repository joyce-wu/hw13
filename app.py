'''
Joyce Wu
Softdev1 pd07
HW13-- A RESTful Journey Skyward
2017-11-09
'''

from flask import Flask, render_template, request
import xmltodict
import urllib2
import json

app = Flask(__name__)

uResp = urllib2.urlopen('https://www.goodreads.com/book/title.xml?author=Arthur+Conan+Doyle&key=odpPCEKyDD92ffeGLZHgag&title=Hound+of+the+Baskervilles')
info = uResp.read()
d = xmltodict.parse(info) #converts xml file to dictionary
print(d)

@app.route("/")
def hello(): #dictionary very confusing
    title = d['GoodreadsResponse']['book']['title']
    image = d['GoodreadsResponse']['book']['image_url']
    review = d['GoodreadsResponse']['book']["description"]
    return render_template("base.html", title=title, image=image, explan=review)

if __name__ == "__main__":
    app.debug = True
    app.run()
