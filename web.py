#!/usr/bin/python3

from flask import Flask, redirect, url_for, request

app = Flask(__name__)
 
@app.route('/')
def hello_world():
        return 'This is my new shiny Flask app'

 
if __name__ == '__main__':
    app.run(debug=True)

