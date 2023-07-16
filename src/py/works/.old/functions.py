
def listDbs():
    query = "SHOW DATABASES"
    queryDb(query)

def createTable():
    query = "CREATE TABLE Person (name VARCHAR(50), age smallint UNSIGNED, personID int PRIMARY KEY AUTO_INCREMENT)"
    queryDb(query, commit=True)

def showTable(table):
    query = f"DESCRIBE {table}"
    queryDb(query)

def insertPerson(name, age):
    query = f"INSERT INTO Person (name, age) VALUES ('{name}', {age})"
    queryDb(query, commit=True)

def listPerson():
    query = "SELECT * FROM Person"
    queryDb(query)

def deletePerson(name):
    query = f"DELETE FROM Person WHERE name='{name}'"
    queryDb(query, commit=True)

if __name__ == '__main__':
    createTable()
    showTable("Person")
    insertPerson("Thomas", 19)
    insertPerson("Hiram", 33)
    deletePerson("Thomas")
    deletePerson("Hiram")
    listPerson()
