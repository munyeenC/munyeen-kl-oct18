# -*- coding: utf-8 -*-
"""
Created on Thu Nov 22 10:08:40 2018

@author: munyeen.chong
"""

from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def formpage():
    return render_template('customerform.html')

@app.route("/submit",methods=['POST'])
def submitpage():
    txtValue = request.form['cus_fname']
    print("received:" + txtValue);
    return render_template('customersubmit.html',inputName=txtValue)

if __name__=="__main__":
    app.run()