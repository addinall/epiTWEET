# epiTWEET - PYTHON Web App

## Bioinformatic project that datamines social media discovering epidemic transmission of disease

###  Mark Addinall.  November 2015

-----


Bioinformatic project that datamines social media discovering epidemic transmission of disease.
This application uses the Twitter global datasets to discover people tweeting symptoms of
disease globally.  By using clustering techniques and time series analysis, we should be able
to estimate the R0 of a POSSIBLE disease and observe the SIR (Susceptable, Infected, Removed) data points based on the frequency of mined tweets.

GOOGLE does something similar with proprietry data aimed at identifying influenza epidemics/pandemics.

Twitter data is available in an open manner.  APIs are readily available.

This project is using AngularJS, Javascript, HTML5, CSS3, Bootstrap and Python.  Later we will add some limited local store using Mongo/Redix.

I will be developing the REST server in Python and using Angular REST to consume the data mining results.  I just had a 
look at a number of frameworks to do this and they are all to big and messy.  So I'll roll my own as per usual.

Perhaps *Mike Stealthman* will be joining the team to make a start on the client side, mailnly consuming CRUD/REST services from a HTML5/AngularJS POV.  Once the RESTful back end of mine is finished, and we have a handle on Angular2 and how it functions, then we can branch the toolset into one or more business ideas and leave me to play with viral infections!

