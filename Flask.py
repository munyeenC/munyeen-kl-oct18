# -*- coding: utf-8 -*-
"""
Created on Wed Nov 21 10:19:23 2018

@author: munyeen.chong
"""

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello!"

if __name__=="__main__":
    app.run()

        

        