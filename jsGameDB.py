import mysql.connector

HOST="localhost"
USER="root"
PASSWORD="onlyroot"
PORT="3306"
DATABASE="jsgame"

def select(sql):
    con = mysql.connector.connect(host=HOST, password=PASSWORD, user=USER, port=PORT, database=DATABASE)
    mycursor = con.cursor(dictionary=True)
    mycursor.execute(sql)
    return mycursor.fetchall()

def insert(sql):
    con = mysql.connector.connect(host=HOST, password=PASSWORD, user=USER, port=PORT, database=DATABASE)
    mycursor = con.cursor(dictionary=True)
    mycursor.execute(sql)
    con.commit()
    mycursor.close()

def update(sql):
    con = mysql.connector.connect(host=HOST, password=PASSWORD, user=USER, port=PORT, database=DATABASE)
    mycursor = con.cursor(dictionary=True)
    mycursor.execute(sql)
    con.commit()
    mycursor.close()