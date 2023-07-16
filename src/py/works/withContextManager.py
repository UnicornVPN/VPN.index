from mysql.connector import connect, Error


def connectDbEngine():
    try:
        with connect(
            host="localhost",
            user="root",
            password="144000"
        ) as connection:
            print(connection)
    except Error as e:
        print(e)

def connectDb():
    try:
        with connect(
            host="localhost",
            user="root",
            password="144000",
            database="mydatabase"
        ) as connection:
            cursor = connection.cursor()
            print(connection)
    except Error as e:
        print(e)

def listDbs():
    try:
        with connect(
            host="localhost",
            user="root",
            password="144000"
        ) as connection:
            cursor = connection.cursor()
            cursor.execute("SHOW DATABASES")
            for x in cursor:
                print(x)
    except Error as e:
        print(e)

def createTable():



if __name__ == '__main__':
    # connectDbms()
    listDbs()