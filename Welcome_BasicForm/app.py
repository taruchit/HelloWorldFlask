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
@app.route('/',methods=["GET","POST"])
def rootPage():
    name=""
    if request.method=="POST" and "username" in request.form:
        name=request.form.get("username")
    return render_template("index.html",name=name)


app.run()