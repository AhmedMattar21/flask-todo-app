import sqlite3
import pymysql
import os

class conn:
    "DB Connection Handler with MySQL"

    def connect():
        # get all environment variables
        mySqlHost = os.environ.get('MYSQL_HOST')
        mySqlUser = os.environ.get('MYSQL_USER')
        mySqlPassword = os.environ.get('MYSQL_ROOT_PASSWORD')
        mySqlDb= os.environ.get('MYSQL_DB')
        try:
            db_conn = pymysql.connect(host=mySqlHost, user=mySqlUser, password=mySqlPassword, db=mySqlDb)
            print(f'\U00002705 Database Connected Successfully! \n')
            
        except:
            print(f'\n\n\U0001F631  I cannot connect the database on {mySqlHost} \n\n\n')
            exit()
        return db_conn
    

    def init_db():
        db = conn.connect()
        cr = db.cursor()

        file = open("init.sql", "r")
        strc = file.readlines()
        csql = conn.clean_sql(strc)
        # print(f'DEBUG: {csql} \n\n\n')
        cr.execute(csql)
        db.commit()

    def NonReturnQuery(sql):
        db = conn.connect()
        cr = db.cursor()
        csql = conn.clean_sql(sql)
        cr.execute(csql)
        db.commit()

    # a methon for removing \n and \t form the sql string
    def clean_sql(sql):
        cleansql = ""
        for line in sql:
            cln = line.split("\n")
            cln[0] = cln[0].replace("\t", "")
            cleansql = cleansql + cln[0]
        return cleansql

    def get_nextID(table, id):
        db = conn.connect()
        cr = db.cursor()
        try:
            cr.execute(f"SELECT MAX({id}) FROM {table} ")
            maxID = cr.fetchone()
            maxID = maxID[0]
            nextID = maxID + 1
            return nextID
        except:
            return 1

    def returnQuery(sql):
        db = conn.connect()
        cr = db.cursor()
        try:
            cr.execute(sql)
            res = cr.fetchall()
            return res
        except:
            return " - "
