from mysql.connector import connect, Error

def queryDb(func):
    with connect(
        host="localhost",
        user="vpn",
        password="base12universe"
    ) as connection:
        func(connection)

def listDbs(connection):
    show_db_query = "SHOW DATABASES"
    with connection.cursor() as cursor:
        cursor.execute(show_db_query)
        for db in cursor:
            print(db)


# listall()
queryDb(listDbs)