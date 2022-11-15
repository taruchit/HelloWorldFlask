# -*- coding: utf-8 -*-
"""
Created on Wed Nov 16 01:24:38 2022

@author: pc
"""

from flask import Flask

app=Flask(__name__)

@app.route('/')
def rootPage():
    return "Hello World, this is my root page in Flask app."

@app.route('/home')
def homePage():
    return"Hello World, this is my home page in Flask app"

@app.route('/second')
def secondPage():
    return "Hello World, this is my second page in Flask app"

app.run()