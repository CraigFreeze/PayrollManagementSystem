# Running Code
- The Database has been omitted from github. To build the database, run "queries.py"

# Overview

As a software engineer, I identified a problem that I found: record keeping in the work force. As such, this was my first version and attempt at solivng this problem. As per the engineering design process, this would be attempt one at several iterations at improving software that is workplace ready.

My software is a Payroll management system where an employer can input employees and crude record keeping of how many hours that given individual worked and are payed. There is a toggle to quickly see an overview of your records, and then at a glance you can see the most worked employee and how many people worked.

The purpose is to create help employers better store and manage their employees, which in turn would create a better work experience for the ground floor. It doubles as an opportunity to learn linking strategies between an SQL relational database and UI.

[Software Demo Video](https://youtu.be/hU91ov54DXY)

# Relational Database

I am using SQLITE3. It is one of the simplist relationabl database frameworks, but gives a taste and look at all the necessary functions: Select, insert, update, aggregate, join, etc. For a small database on a local machine, it performs well.

I created two tables that have a common column of name. And in whole the database contains employee information (name, job, and email) and also pay roll information (name, hours worked, and hourly pay).

# Development Environment

My IDE is VSCode, and I used PYQT for the GUI. This was a large learning step in the process as many of the elements had unfamiliar linking methods. Since QT was originally designed for development in C++, I was exposed to new area that I wasn't previously privyy to.

I used python version 3.10.5 and pyuic6 (warning: most online resources still use pyuic5 (before the overhaul)). I also used a great deal of SQL through SQLITE3 which comes included in python.The libraries that I primarily used are within pyqt: QSqlDatabase, QSqlQuery.

# Useful Websites

- [PYQT Tutorial](https://realpython.com/python-pyqt-gui-calculator/)
- [Web Site Name](https://doc.qt.io/qtforpython/PySide6/QtSql/QSqlQuery.html#PySide6.QtSql.PySide6.QtSql.QSqlQuery.exec)
- [W3 Schools Joins](https://www.w3schools.com/sql/sql_join_right.asp)
- [String Interpolation](https://www.programiz.com/python-programming/string-interpolation)
- [SQLITE Documenation](https://www.sqlite.org/datatype3.html)
- [W3 Schools Aggregate](https://www.w3schools.com/sql/sql_count_avg_sum.asp)


# Future Work

- Add styling for a cleaner asthetic
- Add more helpful fields
- Create a user dashboard
- Create an admin dashboard
- Create a location for employees to punch in and out like a time card