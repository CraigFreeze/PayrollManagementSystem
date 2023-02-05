import sys

from PyQt6.QtSql import QSqlDatabase, QSqlQuery
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QMessageBox,
    QTableWidget,
    QTableWidgetItem,
)

class Contacts(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("QTableView Example")
        self.resize(450, 250)
        # Set up the view and load the data
        self.view = QTableWidget()
        self.view.setColumnCount(4)
        self.view.setHorizontalHeaderLabels(["ID", "Name", "Job", "Email"])
        query = QSqlQuery("SELECT id, name, job, email FROM contacts")
        while query.next():
            rows = self.view.rowCount()
            self.view.setRowCount(rows + 1)
            self.view.setItem(rows, 0, QTableWidgetItem(str(query.value(0))))
            self.view.setItem(rows, 1, QTableWidgetItem(query.value(1)))
            self.view.setItem(rows, 2, QTableWidgetItem(query.value(2)))
            self.view.setItem(rows, 3, QTableWidgetItem(query.value(3)))
        self.view.resizeColumnsToContents()
        self.setCentralWidget(self.view)

def createConnection():
    con = QSqlDatabase.addDatabase("QSQLITE")
    con.setDatabaseName("contacts.sqlite")
    if not con.open():
        QMessageBox.critical(
            None,
            "QTableView Example - Error!",
            "Database Error: %s" % con.lastError().databaseText(),
        )
        return False
    return True

app = QApplication(sys.argv)
if not createConnection():
    sys.exit(1)
win = Contacts()
win.show()
sys.exit(app.exec())

# import sys

# from PyQt6.QtSql import QSqlDatabase
# from PyQt6.QtWidgets import QApplication, QMessageBox, QLabel

# # Create the connection
# con = QSqlDatabase.addDatabase("QSQLITE")
# con.setDatabaseName("employee")

# # Create the application
# app = QApplication(sys.argv)

# # Try to open the connection and handle possible errors
# if not con.open():
#     QMessageBox.critical(
#         None,
#         "App Name - Error!",
#         "Database Error: %s" % con.lastError().databaseText(),
#     )
#     sys.exit(1)

# # Create the application's window
# win = QLabel("Connection Successfully Opened!")
# win.setWindowTitle("App Name")
# win.resize(200, 100)
# win.show()
# sys.exit(app.exec())

# # import sqlite3

# # conn = sqlite3.connect('employee.db')

# # c = conn.cursor() #database uses this cursor to modify the database

# # c.execute('''CREATE TABLE employees (
# #             employee_id integer,
# #             first text,
# #             last text,
# #             email text, 
# #             phone integer, 
# #             address1 text, 
# #             address2 text, 
# #             state text, 
# #             zipcode integer, 
# #             ssn text, 
# #             hour_pay integer, 
# #             salary_pay integer, 
# #             salary text, 
# #             hourly text, 
# #             partime integer, 
# #             fulltime integer
# #         )''')

# # def insert_employee(employee):
# #     with conn:
# #         c.execute('''INSERT INTO employees VALUES (
# #             :employee_id,
# #             :first,
# #             :last,
# #             :email, 
# #             :phone, 
# #             :address1, 
# #             :address2, 
# #             :state, 
# #             :zipcode, 
# #             :ssn, 
# #             :hour_pay, 
# #             :salary_pay, 
# #             :salary, 
# #             :hourly, 
# #             :partime, 
# #             :fulltime)'''
# #             , {'employee_id': employee.employee_id, 'first': employee.first, 'last': employee.last,'email': employee.email, 'phone': employee.phone, 'address1': employee.address1, 'address2': employee.address2, 'state': employee.state, 'zipcode': employee.zipcode, 'ssn': employee.ssn, 'hour_pay': employee.hour_pay, 'salary_pay': employee.salary_pay, 'salary': employee.salary, 'hourly': employee.hourly, 'partime': employee.partime, 'fulltime': employee.fulltime})

# # def update_pay(employee):
# #     pass

# # def update_phone(employee):
# #     pass

# # def update_email(employee):
# #     pass

# # def remove_employee(employee):
# #     pass

# # conn.commit()
# # conn.close() #Stops connection to srever


def filler():
    # # Creating a query for later execution using .prepare()
    # insertDataQuery = QSqlQuery()
    # insertDataQuery.prepare(
    #     """
    #     INSERT INTO contacts (
    #         name,
    #         job,
    #         email
    #     )
    #     VALUES (?, ?, ?)
    #     """
    # )

    # # Sample data
    # data = [
    #     ("Joe", "Senior Web Developer", "joe@example.com"),
    #     ("Lara", "Project Manager", "lara@example.com"),
    #     ("David", "Data Analyst", "david@example.com"),
    #     ("Jane", "Senior Python Developer", "jane@example.com"),
    # ]

    # # Use .addBindValue() to insert data
    # for name, job, email in data:
    #     print(name)
    #     insertDataQuery.addBindValue(name)
    #     print(job)
    #     insertDataQuery.addBindValue(job)
    #     print(email)
    #     insertDataQuery.addBindValue(email)
    #     insertDataQuery.exec()

    # print("successful query?", query.exec("SELECT name, job, email FROM employees"))
    # print("active: ", query.isActive())
    # print("is select: ", query.isSelect)

    # query.exec(
    #     '''
    #     INSERT INTO contacts (
    #         name, job, email
    #     )
    #     VALUES(
    #         "Joe", "Teacher", "joe@example.com"
    #     )
    #     '''
    # )
    pass