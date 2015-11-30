## CAPTAIN SLOG
## vim: set expandtab tabstop=4 shiftwidth=4 autoindent smartindent:
## File         :   twit_init.py 
## System       :   pyTWEET
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

import tweepy
from tweepy import OAuthHandler

def initTwit():

    ''' This function starts the Twitter API and handles the
        authorisation by passing MY secret keys.
        This could be a security worry in the future.  These
        key should NOT be stored under the html_public area.
        I need to swing them up a level and restrict even read access.
        TODO: '''

    consumer_key        = 'edh61ZLLRwwJeobPzrA69nrxn'
    consumer_secret     = 'TewpeMfmEDlIYK2vCWoojQSUxW2gBngsL6t6ir72YHVpoBwGLI'

    access_token        = '17554806-cEQu158Fanl41XJf6Latc5EREFMvXpkiH4t6y89gd'
    access_token_secret = 'm5YLxVJK4RAATBPRegjzUtpcIcCyglxJvP1SDp1vv7W2g'

    success             = True

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    if (auth):
        auth.set_access_token(access_token, access_token_secret)
    else:
        print("Error: - auth not set")
        success = False

    api = tweepy.API(auth)
    if (api):
        public_tweets = api.home_timeline()
        if (public_tweets):
            for tweet in public_tweets:
                print(tweet.text, end="\n\n")
        else:
            print("Error: - no public tweets")
            success = False
    else:
        print("Error: - api not set")
        success = False

    return success

#test it


if initTwit():
    print('Done \n')



