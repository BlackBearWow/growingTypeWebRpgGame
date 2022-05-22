import mysql.connector

HOST="localhost"
USER="root"
PASSWORD="onlyroot"
PORT="3306"
DATABASE="jsGame"

def createDatabase(sql):
    con = mysql.connector.connect(host=HOST, password=PASSWORD, user=USER, port=PORT, database="mysql")
    mycursor = con.cursor(dictionary=True)

    mycursor.execute(sql)
    mycursor.close()
    con.close()
    
def insertSql(sql):
    con = mysql.connector.connect(host=HOST, password=PASSWORD, user=USER, port=PORT, database="jsGame")
    mycursor = con.cursor(dictionary=True)

    mycursor.execute(sql)
    con.commit()
    mycursor.close()
    con.close()

f = open("./database/createDatabase.sql", "rt")
createDatabase(f.read())
f.close()
# id passwd nickname level exp speed wbLimitQuantity wbLen money
insertSql('insert into account values ("admin", "1234", "admin", 20, 30, 4.0, 5, 5, 5000);')
insertSql('insert into account values ("guest", "guest", "guest", 20, 1, 2.0, 3, 3, 5000);')
insertSql('insert into account values ("sce6544", "54540d0", "차돌짬뽕", 10, 1, 2.0, 3, 3, 5000);')
insertSql('insert into account values ("se654c", "c545cw0", "김치찌개", 10, 1, 2.0, 3, 3, 5000);')