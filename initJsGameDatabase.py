import mysql.connector
import hashlib

HOST="localhost"
USER="root"
PASSWORD="onlyroot"
PORT="3306"
DATABASE="jsgame"

def createDatabase(sql):
    con = mysql.connector.connect(host=HOST, password=PASSWORD, user=USER, port=PORT, database="mysql")
    mycursor = con.cursor(dictionary=True)

    mycursor.execute(sql)
    mycursor.close()
    con.close()
    
def insertSql(sql):
    con = mysql.connector.connect(host=HOST, password=PASSWORD, user=USER, port=PORT, database="jsgame")
    mycursor = con.cursor(dictionary=True)

    mycursor.execute(sql)
    con.commit()
    mycursor.close()
    con.close()

f = open("./database/createDatabase.sql", "rt")
# createDatabase(f.read())
f.close()
# id passwd nickname level exp speed wbLimitQuantity wbLen money
insertSql('insert into account values ("admin", "'+hashlib.sha256("1234".encode()).hexdigest()+'", "admin", 20, 30, 4.0, 5, 5, 5000);')
insertSql('insert into account values ("guest", "'+hashlib.sha256("guest".encode()).hexdigest()+'", "guest", 20, 1, 2.0, 3, 3, 5000);')
insertSql('insert into account values ("sce6544", "'+hashlib.sha256("54e1c6s".encode()).hexdigest()+'", "차돌짬뽕", 10, 1, 2.0, 3, 3, 5000);')
insertSql('insert into account values ("se654c", "'+hashlib.sha256("3ksc90ix".encode()).hexdigest()+'", "김치찌개", 10, 1, 2.0, 3, 3, 5000);')
insertSql('insert into account values ("pat0407", "'+hashlib.sha256("asdf".encode()).hexdigest()+'", "김치찌개", 10, 1, 2.0, 3, 3, 5000);')