import sqlite3

## Connectt to SQlite
connection=sqlite3.connect("student.db")

# Create a cursor object to insert record,create table

cursor=connection.cursor()

## create the table
table_info="""
Create table STUDENT(NAME VARCHAR(25),PHYSICS INT, CHEMISTRY INT, MATH INT, BIOLOGY INT, TOTAL INT);

"""
cursor.execute(table_info)

## Insert Some more records

cursor.execute('''Insert Into STUDENT values('Aarav', 75, 82, 90, 88, 335)''')
cursor.execute('''Insert Into STUDENT values('Ishita', 67, 71, 83, 79, 300)''')
cursor.execute('''Insert Into STUDENT values('Kunal', 88, 85, 80, 77, 330)''')
cursor.execute('''Insert Into STUDENT values('Priya', 74, 79, 92, 85, 330)''')
cursor.execute('''Insert Into STUDENT values('Ravi', 65, 70, 75, 80, 290)''')
cursor.execute('''Insert Into STUDENT values('Sneha', 90, 88, 87, 89, 354)''')
cursor.execute('''Insert Into STUDENT values('Laksh', 60, 65, 70, 75, 270)''')
cursor.execute('''Insert Into STUDENT values('Anika', 82, 85, 91, 90, 348)''')
cursor.execute('''Insert Into STUDENT values('Rahul', 85, 80, 89, 82, 336)''')
cursor.execute('''Insert Into STUDENT values('Naina', 72, 68, 75, 80, 295)''')
cursor.execute('''Insert Into STUDENT values('Varun', 77, 80, 85, 83, 325)''')
cursor.execute('''Insert Into STUDENT values('Diya', 66, 70, 74, 69, 279)''')
cursor.execute('''Insert Into STUDENT values('Arjun', 89, 90, 87, 91, 357)''')
cursor.execute('''Insert Into STUDENT values('Meera', 78, 79, 82, 77, 316)''')
cursor.execute('''Insert Into STUDENT values('Rohan', 92, 88, 84, 85, 349)''')
cursor.execute('''Insert Into STUDENT values('Tara', 65, 68, 72, 75, 280)''')
cursor.execute('''Insert Into STUDENT values('Siddharth', 81, 83, 89, 87, 340)''')
cursor.execute('''Insert Into STUDENT values('Leela', 70, 75, 78, 80, 303)''')
cursor.execute('''Insert Into STUDENT values('Manav', 73, 77, 79, 75, 304)''')
cursor.execute('''Insert Into STUDENT values('Parvati', 62, 68, 70, 71, 271)''')
cursor.execute('''Insert Into STUDENT values('Raj', 88, 85, 83, 90, 346)''')
cursor.execute('''Insert Into STUDENT values('Aditi', 91, 89, 87, 88, 355)''')
cursor.execute('''Insert Into STUDENT values('Dev', 75, 72, 80, 78, 305)''')
cursor.execute('''Insert Into STUDENT values('Gauri', 68, 70, 72, 74, 284)''')
cursor.execute('''Insert Into STUDENT values('Vikram', 86, 83, 81, 82, 332)''')
cursor.execute('''Insert Into STUDENT values('Shreya', 80, 78, 85, 86, 329)''')
cursor.execute('''Insert Into STUDENT values('Aakash', 64, 66, 71, 75, 276)''')
cursor.execute('''Insert Into STUDENT values('Anjali', 90, 92, 88, 91, 361)''')
cursor.execute('''Insert Into STUDENT values('Kiran', 72, 74, 79, 77, 302)''')
cursor.execute('''Insert Into STUDENT values('Mohan', 83, 80, 85, 82, 330)''')

## Disspaly ALl the records

print("The isnerted records are")
data=cursor.execute('''Select * from STUDENT''')
for row in data:
    print(row)

## Commit your changes int he databse
connection.commit()
connection.close()