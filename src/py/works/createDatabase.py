import mysql.connector


def connect():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="144000"
    )
    return mydb

def cursor():
    mydb = connect()
    mycursor = mydb.cursor()
    return mycursor

def create():
    mycursor = cursor()
    mycursor.execute("CREATE DATABASE mydatabase")
    mydb.commit()
    mydb.close()

def list(mydb):
    mycursor.execute("SHOW DATABASES")

if __name__ == '__main__':
    mydb = connect()
    mycursor = mydb.cursor()

    mycursor.execute("SHOW DATABASES")
    for x in mycursor:
        print(x)

    mydb.close()
