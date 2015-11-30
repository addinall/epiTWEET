##  CAPTAIN SLOG
##  vim: set expandtab tabstop=4 shiftwidth=4 autoindent :
##  File        :   app_calsses.py 
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


class Base:
    ''' This is the underlying encapsulated structure for all of our application objects.
        We are using a traditional OOD/OOP approach to this tool set and application
        suite.  Although for the REST service we will introduce a VERY minimal
        MVC, the rest (sic) of our objects are coming straight from the purists book.

        These object in here will make use of staked inheretance, which is
        the only type of plymorphism I allow. '''



class AppObject(Base):
    ''' This is the next layer on the onion for our larger application objects.
        The reason this step exists is that smaller/utility/tempory application
        object will also inherate from class Base. '''


class Person(AppObject):


class Member(Person):


class CustomerContact(Person):


class SupplierContact(Person):


class Staff(Person):


class Administrator(Staff):


