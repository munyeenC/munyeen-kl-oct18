# -*- coding: utf-8 -*-
"""
Created on Wed Nov 21 10:19:23 2018

@author: munyeen.chong
"""

from flask import Flask
app = Flask(__name__)

@app.route("/")
def welcome():
   return "Welcome World! </p> <a href=http://127.0.0.1:5000/hello> Hello </a></p> <a href=http://127.0.0.1:5000/goodbye> Goodbye </a>"

@app.route("/hello")
def hello():
   return "Hello!"
   
@app.route("/goodbye")
def goodbye():
   return "Goodbye!"

if __name__=="__main__":
   app.run()
    
  

