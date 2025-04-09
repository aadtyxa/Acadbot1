import sqlite3

connection=sqlite3.connect("student.db")
cursor=connection.cursor()

table_info="""
Create table STUDENT(NAME VARCHAR(25),CLASS VARCHAR(25),
SECTION VARCHAR(25),MARKS INT);

"""
cursor.execute(table_info)

cursor.execute('''Insert Into STUDENT values('Aditya','Data Science','A',90)''')
cursor.execute('''Insert Into STUDENT values('Rishabh','Data Science','B',100)''')
cursor.execute('''Insert Into STUDENT values('Ayush','Data Science','A',86)''')
cursor.execute('''Insert Into STUDENT values('khushi','Data Science','B',50)''')
cursor.execute('''Insert Into STUDENT values('Harsh','Data Science','A',35)''')

print("The inserted records are")

data=cursor.execute('''Select * From STUDENT''')

for row in data:
    print(row)

    connection.commit()
    connection.close()