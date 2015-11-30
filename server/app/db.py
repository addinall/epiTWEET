## CAPTAIN SLOG
## vim: set expandtab tabstop=4 shiftwidth=4 autoindent smartindent:
## File         : db.py 
## System       : epiTWEET
## Date         : May 19 2015
## Author       : Mark Addinall
## Synopsis     : Object oriented connect from the Python RESTful transactions
##                to a database.  This is being developed as database agnostic,
##                however, this time we will start with postgreSQL.
##                This thing handles the lower level calls to whatever
##                database is installed.  It provides that level of abstraction
##                to the CRUD REST API.
##             
##
## -------------------------------

import psycopg2

#--------------
class Database:
    active = False

    def __init__(self, db_unit_test, db_name, db_user, db_pass, db_host, db_port, db_brand):

        self.test       = db_unit_test      # by building the unit testing functionality
                                            # INTO the actual fundemental classes, we
                                            # can choose our lebel of testing granurality 
                                            # over the lifespan of the system
        self.name       = db_name
        self.user       = db_user
        self.password   = db_pass
        self.host       = db_host
        self.port       = db_port

        self.brand      = db_brand          # not used just at the moment, but
                                            # it will be very shortly.  Once I am
                                            # happy with the structure and 
                                            # robstness of this model we shall
                                            # add in
                                            # mySQL
                                            # Mongo
                                            # DB2
                                            # ORACLE (perhaps, Sun have done a good job of
                                            # buggering what was once the best of the lot)
    #----------------
    def connect(self):

        ''' This next bit looks odd.  Python is still somewhat finicky
            with strings, postgreSQL doubly so, and the factory in
            psycopg2 can not seem to make a choice which side to be
            on.  The syntax ends up being quite horrid, but allows us
            to keep the same API agnostic of database brand. '''

        info = """
           dbname=%s  
           user=%s 
           password=%s 
           host=%s 
           port=%s 
        """ % (self.name, self.user, self.password, self.host, self.port)
       
        try:
            self.conn = psycopg2.connect(info)
        except:
            print "DB faied"                # error classes going in at the end
                                            # of the week so we have automated
                                            # testing and some self healing
        if self.test:
            if self.conn:
                print "Opened database successfully"



# -------------- End of class Database definition -----------------



#-------------------------------------
db_instance = Database( True,
                        "python-test",
                        "addinall",
                        "S0laris7.1",
                        "127.0.0.1",
                        "5432",
                        "postgreSQL")

db_instance.connect()


