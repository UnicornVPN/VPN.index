from mysql.connector import connect, Error
"""From: https://www.w3schools.com/sql/sql_quickref.asp, https://youtu.be/91iNR0eG8kE, https://realpython.com/python-mysql/"""

class Db:
    def __init__(self, database="mydatabase", host="localhost", user="root", password="144000"):
        self.database = database
        self.host = host
        self.user = user
        self.password = password

    def createDb(self):
        query = f"CREATE DATABASE {self.database}"

        with connect(
            host=self.host,
            user=self.user,
            password=self.password
        ) as connection:
            cursor = connection.cursor()
            cursor.execute(query)

    def query(self, sql, commit=False, print=False):
        try:
            with connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            ) as connection:
                cursor = connection.cursor()
                cursor.execute(sql)
                if commit:
                    connection.commit()
                # Print
                if print:
                    for x in cursor:
                        print(x)
                # Return
                return cursor
        except Error as e:
            print(e)

    def queryPrint(self, sql, commit=False):
        with connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
        ) as connection:
            cursor = connection.cursor()
            cursor.execute(sql)
            if commit:
                connection.commit()
            # Return
            return cursor
    def listDbs(self):
        sql = "SHOW DATABASES"
        list_db = self.queryPrint(sql)
        for x in list_db:
            print(x)



if __name__ == '__main__':
    db = Db("freevpns")
    # db.createDb()
    db.listDbs()