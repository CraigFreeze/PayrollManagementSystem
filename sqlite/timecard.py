import sqlite3

conn = sqlite3.connect('employee.db')

c = conn.cursor() #database uses this cursor to modify the database

c.execute('''CREATE TABLE time_card (
            employee_id integer,
            clock_in text,
            clock_out text, 
            meal integer
        )''')

def clock_in(timeCard):
    pass #creates a new row 

def clock_out(timeCard):
    pass #updates the row from that same day with the correct out time, clocking out is also where you take in if they ate a meal or not

conn.commit()
conn.close() #Stops connection to srever