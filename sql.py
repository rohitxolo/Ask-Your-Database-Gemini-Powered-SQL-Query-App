import sqlite3

# connect to sqlite
connection = sqlite3.connect("student.db")

# create a cursor object to insert record, create table, retrieve
cursor = connection.cursor()

# create the table, checking if it already exists
table_info = """
CREATE TABLE IF NOT EXISTS STUDENT (
    NAME VARCHAR(25),
    CLASS VARCHAR(25),
    SECTION VARCHAR(25),
    MARKS INT
);
"""

cursor.execute(table_info)

# Insert some more records
cursor.execute('''INSERT INTO STUDENT VALUES('Krish', 'Data Science', 'A', 90)''')
cursor.execute('''INSERT INTO STUDENT VALUES('Sudanshu', 'Data Science', 'B', 100)''')
cursor.execute('''INSERT INTO STUDENT VALUES('Darius', 'Data Science', 'A', 86)''')
cursor.execute('''INSERT INTO STUDENT VALUES('Vikash', 'DEVOPS', 'A', 50)''')
cursor.execute('''INSERT INTO STUDENT VALUES('Dipesh', 'DEVOPS', 'A', 35)''')

# Display all the records
print("The inserted records are:")

data = cursor.execute('''SELECT * FROM STUDENT''')
for row in data:
    print(row)

# Commit and close the connection
connection.commit()
connection.close()
