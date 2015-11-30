## CAPTAIN SLOG
## vim: set expandtab tabstop=4 shiftwidth=4 autoindent:
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
import logging

#--------------
class Database:

    __active = False                        # as with classical OOD, we are NOT goint
                                            # to let the world muck around with our
                                            # internal properties.  Anything we THINK
                                            # a service user should be able to change
                                            # (not much) will get appropriate methods

    def __init__(self, db_unit_test, db_name, db_user, db_pass, db_host, db_port, db_brand):

        self.test       = db_unit_test      # by building the unit testing functionality
                                            # INTO the actual fundemental classes, we
                                            # can choose our lebel of testing granurality 
                                            # over the lifespan of the system
        if self.test:                       # turn on trace if required
            logging.basicConfig(filename='debug_db.log', level=logging.DEBUG)

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
            to keep the same API agnostic of database brand. 
            This METHOD is PUBLIC, but most of the PROPERTIES
            are not.  This allows the application or middleware ORB
            some discrection in when to start transaction processing. 
            For example, the CSS people may want to run the application
            whilst not connected to a DBMS server.  
        '''

        info = """
           dbname=%s  
           user=%s 
           password=%s 
           host=%s 
           port=%s 
        """ % (self.name, self.user, self.password, self.host, self.port)
       
        try:
            self.__conn = psycopg2.connect(info)
        except:
            logging.critical("DB faied")        # error classes going in at the end
                                                # of the week so we have automated
                                                # testing and some self healing
        if self.test:
            if self.__conn:
                logging.info("Opened database successfully")

        self.__cursor = self.__conn.cursor()    # and get a cursor to use for the session.
                                                # Make it PRIVATE


    #---------------------------
    def __create_test_database():

        ''' this is here so that during development we can create a fresh set of tables
            without bothering one of the DBAs, ie., me.  It can stay in the system
            for quite a while.  Possibly forever if I am going to be the only
            user of the toolkit.

            If you have forked this and have an intention of going into
            a PRODUCTION environment, I would guggest this be removed.
        '''

        __tweet_requests = """
            CREATE TABLE TWEET-REQUESTS
                (   ID INT      PRIMARY KEY     NOT NULL,
                    NAME        TEXT            NOT NULL,
                    TWEET       TEXT            NOT NULL,
                    LOCATION    CHAR(128)       NOT NULL,
                    NUMBER      INT             NOT NULL);
            """

        self.__cursor.execute(__tweet_requests)

    
    #-------------------------------------------------------------
    # This is now where the public CRUD REST methods live
    #-------------------------------------------------------------

    def CREATE(category, dbase_object):
        ''' This is the C of the CRUD
        '''

        temp = 42


    def REPORT(select_statement):
        ''' This is the R of the CRUD
        '''

        temp = 42


# -------------- End of class Database definition -----------------



#-------------------------------------
db_instance = Database( True,
                        "python-test",
                        "addinall",
                        "S0laris7.1",
                        "127.0.0.1",
                        "5432",
                        "postgreSQL")

if __name__ == '__main__':                  # if we are running stand alone for testing,
    db_instance.connect()                   # connect, else if running as a MODULE, do not.


