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

class User(db.Model):
    id              = db.Column(db.Integer, primary_key=True)
    email           = db.Column(db.String(120), unique=True, nullable=False, info={'validators': Email()})
    password        = db.Column(db.String(80), nullable=False)
    posts           = db.relationship('Post', backref='user', lazy='dynamic')

def __init__(self, email, password):
    self.email      = email
    self.password   = flask_bcrypt.generate_password_hash(password)

def __repr__(self):
    return '<User %r>' % self.email

class Post(db.Model):
    id              = db.Column(db.Integer, primary_key=True)
    title           = db.Column(db.String(120), nullable=False)
    body            = db.Column(db.Text, nullable=False)
    user_id         = db.Column(db.Integer, db.ForeignKey('user.id'))
    created_at      = db.Column(db.DateTime, default=db.func.now())

def __init__(self, title, body):
    self.title      = title
    self.body       = body
    self.user_id    = g.user.id

def __repr__(self):
    return '<Post %r>' % self.title

