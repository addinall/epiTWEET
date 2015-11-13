## CAPTAIN SLOG
## vim: set expandtab tabstop=4 shiftwidth=4 autoindent smartindent:
## File         :   server.py 
## System       :   epiTWEET
## Date         :   November 2015
## Author       :   Mark Addinall
## Synopsis     :   This is a bioinformatic project that datamines social 
##                  media discovering epidemic transmission of disease. 
##                  This application uses the Twitter global datasets to discover 
##                  people tweeting symptoms of disease globally. By using 
##                  clustering techniques and time series analysis, we should be 
##                  able to estimate the R0 of a POSSIBLE disease and observe 
##                  the SIR (Susceptable, Infected, Removed) data points based 
##                  on the frequency of mined tweets.
##
##                  GOOGLE does something similar with proprietry data aimed 
##                  at identifying influenza epidemics/pandemics.
##
##                  Twitter data is available in an open manner. APIs are readily available.
##
##                  This project is using AngularJS, Javascript, HTML5, CSS3, 
##                  Bootstrap and Python. Later we will add some limited local 
##                  store using Mongo/Redix.tool.
##             
##		            This file makes up our initial application server
##                  we are initializing Flask, loading the configuration variables from a 
##                  config file, creating the flask-sqlalchemy, flask-restful objects etc… 
##                  We are also adding some response headers in the after_request function that 
##                  will allow cross-origin resource sharing (CORS). This will allow us to host 
##                  the server (REST API) and the client (AngularJS app) on different domains 
##                  and different subdomains during development, this will also allow us to run 
##                  them on different ports (Example: localhost:8000 and localhost:5000).


import os

from flask import Flask
from flask.ext import restful
from flask.ext.restful import reqparse, Api
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.bcrypt import Bcrypt
from flask.ext.httpauth import HTTPBasicAuth

basedir = os.path.join(os.path.abspath(os.path.dirname(__file__)), '../')

app = Flask(__name__)
app.config.from_object('app.config')

# flask-sqlalchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'app.sqlite')
db = SQLAlchemy(app)

# flask-restful
api = restful.Api(app)

# flask-bcrypt
flask_bcrypt = Bcrypt(app)

# flask-httpauth
auth = HTTPBasicAuth()

@app.after_request
def after_request(response):

    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
    return response

import views


# -------------------------------------------  EOF ----------------------------------
