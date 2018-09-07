# -*- coding: utf-8 -*-
"""
Created on Tue Sep  4 15:22:27 2018

@author: yyy
"""

from flask import Flask
from flask import request
from flask import render_template
app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def home():
    return render_template('home.html')

@app.route('/signin',methods=['GET'])
def signin_form():
    return render_template('form.html')

@app.route('/signin',methods=['POST'])
def signin():
    username = request.form['username']
    password = request.form['password']
    if username == 'bob' and password == 'password':
        return render_template('signin_ok.html',username = username)
    return render_template('form.html',message = 'bad username or password',username = username)

if __name__ == '__main__': 
    app.run()