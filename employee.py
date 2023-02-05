import sys

from PyQt6.QtCore import Qt, QRect
from PyQt6.QtSql import QSqlDatabase, QSqlTableModel, QSqlQuery
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QMessageBox,
    QTableView,
    QWidget, 
    QPushButton, 
    QSpinBox,
    QFormLayout,
    QLineEdit,
    QLabel,
    QTabWidget,
    QComboBox
)

class Employees(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("QTableView Example")
        self.resize(800, 552)
        # Make model 1
        self.model1 = QSqlTableModel(self)
        self.model1.setTable("employees")
        self.model1.setEditStrategy(QSqlTableModel.EditStrategy.OnFieldChange)
        self.model1.setHeaderData(0, Qt.Orientation.Horizontal, "ID")
        self.model1.setHeaderData(1, Qt.Orientation.Horizontal, "Name")
        self.model1.setHeaderData(2, Qt.Orientation.Horizontal, "Job")
        self.model1.setHeaderData(3, Qt.Orientation.Horizontal, "Email")
        self.model1.select()

        # # # Make model 2
        self.model2 = QSqlTableModel(self)
        self.model2.setTable("payroll")
        self.model2.setEditStrategy(QSqlTableModel.EditStrategy.OnFieldChange)
        self.model2.setHeaderData(0, Qt.Orientation.Horizontal, "ID")
        self.model2.setHeaderData(1, Qt.Orientation.Horizontal, "Name")
        self.model2.setHeaderData(2, Qt.Orientation.Horizontal, "hourlyPay")
        self.model2.setHeaderData(3, Qt.Orientation.Horizontal, "hoursWorked")
        self.model2.select()
        
        # ----------Make view---------
        #Tab Widget
        self.tabWidget = QTabWidget(self)
        self.tabWidget.setGeometry(QRect(10, 190, 781, 301))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QWidget()
        self.tab.setObjectName("tab")

        #Inside 1st Tab
        self.view = QTableView(parent=self.tab)
        self.view.setModel(self.model1)
        self.view.resizeColumnsToContents()
        self.view.setGeometry(QRect(10, 10, 751, 251))
        self.tabWidget.addTab(self.tab, "")

        # #Create 2nd Tab
        self.tab_2 = QWidget()
        self.tab_2.setObjectName("tab_2")

        # #Inside 2nd Tab
        self.view = QTableView(parent=self.tab_2)
        self.view.setModel(self.model2)
        self.view.resizeColumnsToContents()
        self.view.setGeometry(QRect(10, 10, 751, 261))
        self.tabWidget.addTab(self.tab_2, "")

        #Delete Row Input
        delete_spinBox = QSpinBox(self,
            value = 1,
            minimum = 1,
            singleStep = 1)
        delete_spinBox.setGeometry(QRect(40, 20, 51, 31))
        self.layout().addWidget(delete_spinBox)

        #Delete Button Creation
        delete_button = QPushButton("Delete by ID", clicked = lambda: deleteFromModel())
        delete_button.setGeometry(QRect(100, 20, 100, 32))
        self.layout().addWidget(delete_button)

        #Form
        self.formLayoutWidget = QWidget(self)
        self.formLayoutWidget.setGeometry(QRect(540, 50, 231, 161))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")

        self.nameLabel = QLabel("field1")
        self.nameLabel.setObjectName("nameLabel")
        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.nameLabel)

        self.nameLineEdit = QLineEdit(self)
        self.nameLineEdit.setObjectName("nameLineEdit")
        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.nameLineEdit)

        self.jobLabel = QLabel("field2")
        self.jobLabel.setObjectName("jobLabel")
        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.jobLabel)

        self.jobLineEdit = QLineEdit(self)
        self.jobLineEdit.setObjectName("jobLineEdit")
        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.jobLineEdit)

        self.emailLabel = QLabel("field3")
        self.emailLabel.setObjectName("emailLabel")
        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.emailLabel)

        self.emailLineEdit = QLineEdit(self)
        self.emailLineEdit.setObjectName("emailLineEdit")
        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.emailLineEdit)

        self.submit_button = QPushButton("Submit", clicked = lambda: insertIntoModel())
        self.submit_button.setObjectName("Submit")
        self.formLayout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.submit_button)

        #Query Form
        self.formLayoutWidget_2 = QWidget(self)
        self.formLayoutWidget_2.setGeometry(QRect(20, 80, 291, 105))
        self.formLayoutWidget_2.setObjectName("formLayoutWidget_2")
        self.formLayout_2 = QFormLayout(self.formLayoutWidget_2)
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.formLayout_2.setObjectName("formLayout_2")

        self.label = QLabel(self)
        self.label.setObjectName("label")
        self.formLayout_2.setWidget(3, QFormLayout.ItemRole.SpanningRole, self.label)

        self.queryButton = QPushButton("Query", clicked = lambda: joinAndSelect())
        self.queryButton.setObjectName("queryButton")
        self.formLayout_2.setWidget(2, QFormLayout.ItemRole.SpanningRole, self.queryButton)

        self.lineEdit = QLineEdit(self)
        self.lineEdit.setObjectName("lineEdit")
        self.formLayout_2.setWidget(1, QFormLayout.ItemRole.SpanningRole, self.lineEdit)

        #Aggregate Form
        self.formLayoutWidget_3 = QWidget(self)
        self.formLayoutWidget_3.setGeometry(QRect(320, 80, 201, 101))
        self.formLayoutWidget_3.setObjectName("formLayoutWidget_3")
        self.formLayout_3 = QFormLayout(self.formLayoutWidget_3)
        self.formLayout_3.setContentsMargins(0, 0, 0, 0)
        self.formLayout_3.setObjectName("formLayout_3")

        self.queryButton_2 = QPushButton("Count", clicked = lambda: aggregate())
        self.queryButton_2.setObjectName("queryButton_2")

        self.formLayout_3.setWidget(0, QFormLayout.ItemRole.FieldRole, self.queryButton_2)
        self.label_2 = QLabel(self)
        self.label_2.setObjectName("label_2")
        self.formLayout_3.setWidget(1, QFormLayout.ItemRole.FieldRole, self.label_2)

        self.pushButton_3 = QPushButton("Max", clicked = lambda: max())
        self.pushButton_3.setObjectName("pushButton_3")

        self.formLayout_3.setWidget(2, QFormLayout.ItemRole.FieldRole, self.pushButton_3)
        self.label_3 = QLabel(self)
        self.label_3.setObjectName("label_3")
        self.formLayout_3.setWidget(3, QFormLayout.ItemRole.FieldRole, self.label_3)

        # self.lineEdit_2 = QLineEdit(self)
        # self.lineEdit_2.setObjectName("lineEdit_2")
        # self.formLayout_3.setWidget(1, QFormLayout.ItemRole.SpanningRole, self.lineEdit_2)

        #Combo Box for selecting Database
        self.comboBox = QComboBox(self)
        self.comboBox.setGeometry(QRect(330, 20, 191, 32))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("payroll")
        self.comboBox.addItem("employees")

        def deleteFromModel():
            deleteRowQuery = QSqlQuery()
            table = self.comboBox.currentText()
            deleteRowQuery.prepare( 
                """
                DELETE FROM %s where id = :val
                """ %table 
            ) 
            deleteRowQuery.bindValue(':val', delete_spinBox.value()) #self.get_row_to_delete()
            deleteRowQuery.exec()
            self.model1.select()
            self.model2.select()

        def insertIntoModel():
            print("HEY I MADE IT HERE -----------")
            insertQuery = QSqlQuery()
            table = self.comboBox.currentText()
            if table == "employees":
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
            elif table == "payroll":
                insertQuery.prepare(
                    """
                    INSERT INTO payroll (
                        name,
                        hourlyPay,
                        hoursWorked
                    )
                    VALUES (?, ?, ?)
                    """
                )
            insertQuery.addBindValue(self.nameLineEdit.text())
            insertQuery.addBindValue(self.jobLineEdit.text())
            insertQuery.addBindValue(self.emailLineEdit.text())
            insertQuery.exec()
            self.model1.select()
            self.model2.select()

        def joinAndSelect():
            joinAndSelectQuery = QSqlQuery()
            joinAndSelectQuery.prepare( 
                """
                SELECT name, job
                FROM employees
                WHERE name = :name
                """
            )
            joinAndSelectQuery.bindValue(':name', self.lineEdit.text())
            print("RESULT: ", joinAndSelectQuery.result())
            joinAndSelectQuery.exec()
            joinAndSelectQuery.first()
            concat = "NAME: " + joinAndSelectQuery.value(0) + " JOB: " + joinAndSelectQuery.value(1) + ""
            self.label.setText(concat)
            print("First Print: ", joinAndSelectQuery.value(0))
            print("Second Print: ",joinAndSelectQuery.value(1))
        
        def aggregate():
            aggregateQuery = QSqlQuery()
            aggregateQuery.prepare( 
                """
                SELECT COUNT(hoursWorked)
                FROM payroll
                """
            )
            aggregateQuery.bindValue(':name', self.lineEdit.text()) 
            print("RESULT: ", aggregateQuery.result())
            aggregateQuery.exec()
            aggregateQuery.first()
            concat = "Total Records: " + str(aggregateQuery.value(0)) + ""
            self.label_2.setText(concat)
            print("First Print: ", aggregateQuery.value(0))
            print("Second Print: ",aggregateQuery.value(1))

        def max():
            maxQuery = QSqlQuery()
            maxQuery.prepare( 
                """
                SELECT MAX(hoursWorked)
                FROM payroll
                """
            )
            maxQuery.bindValue(':name', self.lineEdit.text()) 
            print("RESULT: ", maxQuery.result())
            maxQuery.exec()
            maxQuery.first()
            concat = "Max Hours Worked: " + str(maxQuery.value(0)) + ""
            self.label_3.setText(concat)
            print("First Print: ", maxQuery.value(0))
            print("Second Print: ",maxQuery.value(1))

def createConnection():
    con = QSqlDatabase.addDatabase("QSQLITE")
    con.setDatabaseName("employees.sqlite")
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
win = Employees()
win.show()
sys.exit(app.exec())