# -*- coding: utf-8 -*-
"""
Created on Wed Nov 16 01:24:38 2022

@author: pc
"""

from flask import Flask

app=Flask(__name__)

@app.route('/home')

def welcome():
    return "Hello World, this is my second Flask application with customized decorator"

app.run()