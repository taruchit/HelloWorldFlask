# -*- coding: utf-8 -*-
"""
Created on Wed Nov 16 01:24:38 2022

@author: pc
"""

from flask import Flask, request, render_template

app=Flask(__name__)
'''
@app.route('/')
def rootPage():
    return "Hello World, this is my root page in Flask app."
'''
@app.route('/')
def rootPage():
    return render_template("index.html")

@app.route('/home')
def homePage():
    return"Hello World, this is my home page in Flask app"

@app.route('/second')
def secondPage():
    return "Hello World, this is my second page in Flask app"

@app.route('/method',methods=['GET','POST'])
def method():
    if request.method=='POST':
        return "POST request method was used"
    else:
        return "GET request method was used"
app.run()