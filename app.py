import psycopg2

# Connect to the database, using psycopg2. fill in data from pgadmin to connect
try:
    conn = psycopg2.connect(
        host="localhost",
        port=5432,
        dbname="student",
        user="postgres",
        password="password",
    )
except psycopg2.Error as e:
  
    print("Could not connect\n")
    raise SystemExit(1)

cur = conn.cursor()
print("Connected successfully\n")

#get all students in the database and print them out
def getAllStudents():
    #print all rows in student table
    cur.execute("SELECT * FROM students ORDER BY student_id;")
    for row in cur.fetchall():
        print(row)

#add a student into the table given the first name, last name, email and their enrollment date
def addStudent(first_name, last_name, email, enrollment_date):
    #insert new student into table
    cur.execute(
        "INSERT INTO students (first_name, last_name, email, enrollment_date) "
        "VALUES (%s, %s, %s, %s);",
        (first_name, last_name, email, enrollment_date),
    )
    conn.commit()
    print("Student added\n")

#update a students email given the id and the new email
def updateStudentEmail(student_id, new_email):
    #update student email
    cur.execute(
        "UPDATE students SET email = %s WHERE student_id = %s;",
        (new_email, student_id),
    )
    conn.commit()
    #check if cur increased to make sure the change actually works
    if cur.rowcount > 0:
        print("Email updated\n")
    else:
        print("No student with that ID\n")

#delete a student given the students id and remove it from the database
def deleteStudent(student_id):
    #delete the student given the id
        cur.execute("DELETE FROM students WHERE student_id = %s;", (student_id,))
        conn.commit()
        #check if cur increases to see if it the db has changed
        if cur.rowcount > 0:
            print("Student deleted\n")
        else:
            print("No student with that ID\n")


#testing all the functions individually, prints out the db each time
try:
    print("All students\n")
    getAllStudents()

    input("Press Enter to add a student\n")

    addStudent("Yusuf", "Ahmad", "YusufAhmad@cmail.carleton.ca", "2023-09-05")
    getAllStudents()

    input("Press Enter to update John's email\n")

    updateStudentEmail(1, "john.new@example.com")

    getAllStudents()

    input("\nPress Enter to delete Jim\n")

    deleteStudent(3)
    getAllStudents()

finally:
    #close resources
    cur.close()
    conn.close()
    print("Connection closed\n")