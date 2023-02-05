import sys

from PyQt6.QtSql import QSqlDatabase, QSqlQuery

# Create the connection
con = QSqlDatabase.addDatabase("QSQLITE")
con.setDatabaseName("employees.sqlite")

# Open the connection
if not con.open():
    print("Database Error: %s" % con.lastError().databaseText())
    sys.exit(1)

# Create a query and execute it right away using .exec()
createTableQuery = QSqlQuery()
createTableQuery.exec( 
    """
    CREATE TABLE employees (
        id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
        name VARCHAR(40) NOT NULL,
        job VARCHAR(50),
        email VARCHAR(40) NOT NULL
    )
    """
)
print(con.tables())

createTableQuery.exec( 
    """
    CREATE TABLE payroll (
        id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
        name VARCHAR(40) NOT NULL,
        hourlyPay REAL,
        hoursWorked REAL NOT NULL
    )
    """
)
print(con.tables())

insertQuery = QSqlQuery()
insertQuery.prepare(
    """
    INSERT INTO employees (
        name,
        job,
        email
    )
    VALUES (?, ?, ?)
    """
)

insertQueryPayRoll = QSqlQuery()
insertQueryPayRoll.prepare(
    """
    INSERT INTO payroll (
        name,
        hourlyPay,
        hoursWorked
    )
    VALUES (?, ?, ?)
    """
)

data = [
    ("Joe", "Senior Web Developer", "joe@example.com"),
    ("Lara", "Project Manager", "lara@example.com"),
    ("David", "Data Analyst", "david@example.com"),
    ("Jane", "Senior Python Developer", "jane@example.com"),
]

data_payroll = [
    ("Lara", "18", "10"),
    ("David", "20", "40"),
    ("Craig", "15", "30"),
    ("Craig", "15", "30"),
]

for name, job, email in data:
    insertQuery.addBindValue(name)
    insertQuery.addBindValue(job)
    insertQuery.addBindValue(email)
    insertQuery.exec()

for name, hourlyPay, hoursWorked in data_payroll:
    insertQueryPayRoll.addBindValue(name)
    insertQueryPayRoll.addBindValue(hourlyPay)
    insertQueryPayRoll.addBindValue(hoursWorked)
    insertQueryPayRoll.exec()