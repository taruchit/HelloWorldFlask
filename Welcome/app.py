# -*- coding: utf-8 -*-
"""
Created on Wed Nov 16 01:24:38 2022

@author: pc
"""

from flask import Flask

app=Flask(__name__)

@app.route('/')

def welcome():
    return "Hello World, this is my first Flask application"

app.run()