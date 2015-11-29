##  CAPTAIN SLOG
##  vim: set expandtab tabstop=4 shiftwidth=4 autoindent smartindent:
##  File        :   models.py 
##  System      :   epiTWEET
##  Date        :   November 2015
##  Author      :   Mark Addinall
##  Synopsis    :   This is a bioinformatic project that datamines social 
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
##


from flask import g

from wtforms.validators import Email

from server import db, flask_bcrypt
