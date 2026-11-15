# COMP3005 Assignment: README

## CREATED BY Yusuf Ahmad 101304023

### Description
A student database app implemented with Python and PostgreSQL, the app connects to the database with psycopg2 and can show all students, add a student, update a students email and delete a student. Running app.py does a demo of each one and waits for a key press between steps so the change can be checked in pgAdmin.

#### Video demo
https://www.youtube.com/watch?v=-7T2SA9e-3o

##### Files
students.sql - creates the students table and inserts data 
app.py -  connects to the database and has the four functions 
README.md 

###### How to Run
Make a database called student_db in pgAdmin,
Open the Query Tool on student_db, paste in students.sql and run it,
pip3 install psycopg2-binary,
Open app.py and set your PostgreSQL user and password in the connect line at the top,
python3 app.py, press Enter at each pause to move to the next step. Refresh the students table in pgAdmin to see each change.
