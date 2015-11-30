## CAPTAIN SLOG
## vim: set expandtab tabstop=4 shiftwidth=4 autoindent :
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
##                  config file, creating the db connections, flask-restful objects etc 
##                  We are also adding some response headers in the after_request function that 
##                  will allow cross-origin resource sharing (CORS). This will allow us to host 
##                  the server (REST API) and the client (AngularJS app) on different domains 
##                  and different subdomains during development, this will also allow us to run 
##                  them on different ports (Example: localhost:8000 and localhost:5000).


import db
from flask import Flask, url_for

app = Flask(__name__)

@app.route('/')
def api_root():
    return 'Welcome'

@app.route('/newtweet')
def api_newtweet():
    return 'List of ' + url_for('api_newtweet')

@app.route('/pasttweets/<tweet>')
def api_pasttweets(tweet):
    return 'You are reading ' + tweet

if __name__ == '__main__':
    app.run()



# -------------------------------------------  EOF ----------------------------------
