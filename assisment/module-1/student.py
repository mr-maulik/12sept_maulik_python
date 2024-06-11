import sqlite3

class StudentManagementSystem:
    def __init__(self):
        self.conn = sqlite3.connect('students.db')
        self.cursor = self.conn.cursor()
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS students (
                               student_id TEXT PRIMARY KEY,
                               name TEXT,
                               age INTEGER,
                               contact TEXT,
                               address TEXT)''')
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS marks (
                               student_id TEXT,
                               subject TEXT,
                               marks INTEGER,
                               FOREIGN KEY(student_id) REFERENCES students(student_id))''')
        self.conn.commit()

    def add_student(self, student_id, name, age, contact, address):
        try:
            self.cursor.execute('''INSERT INTO students (student_id, name, age, contact, address)
                                   VALUES (?, ?, ?, ?, ?)''', (student_id, name, age, contact, address))
            self.conn.commit()
            print(f"Student {name} added successfully!")
        except sqlite3.IntegrityError:
            print(f"Student ID {student_id} already exists!")

    def remove_student(self, student_id):
        self.cursor.execute('''DELETE FROM students WHERE student_id = ?''', (student_id,))
        self.cursor.execute('''DELETE FROM marks WHERE student_id = ?''', (student_id,))
        self.conn.commit()
        if self.cursor.rowcount > 0:
            print(f"Student ID {student_id} removed successfully!")
        else:
            print("Student not found!")

    def view_student(self, student_id):
        self.cursor.execute('''SELECT * FROM students WHERE student_id = ?''', (student_id,))
        student = self.cursor.fetchone()
        if student:
            print(f"Student ID: {student[0]}")
            print(f"Name: {student[1]}")
            print(f"Age: {student[2]}")
            print(f"Contact: {student[3]}")
            print(f"Address: {student[4]}")
            self.cursor.execute('''SELECT subject, marks FROM marks WHERE student_id = ?''', (student_id,))
            marks = self.cursor.fetchall()
            if marks:
                print("Marks:")
                for subject, mark in marks:
                    print(f"  {subject}: {mark}")
        else:
            print("Student not found!")

    def view_all_students(self):
        self.cursor.execute('''SELECT * FROM students''')
        students = self.cursor.fetchall()
        if not students:
            print("No students available.")
        else:
            for student in students:
                print(f"\nStudent ID: {student[0]}")
                print(f"Name: {student[1]}")
                print(f"Age: {student[2]}")
                print(f"Contact: {student[3]}")
                print(f"Address: {student[4]}")
                self.cursor.execute('''SELECT subject, marks FROM marks WHERE student_id = ?''', (student[0],))
                marks = self.cursor.fetchall()
                if marks:
                    print("Marks:")
                    for subject, mark in marks:
                        print(f"  {subject}: {mark}")

    def add_student_marks(self, student_id, subject, marks):
        self.cursor.execute('''SELECT 1 FROM students WHERE student_id = ?''', (student_id,))
        if self.cursor.fetchone():
            self.cursor.execute('''INSERT OR REPLACE INTO marks (student_id, subject, marks)
                                   VALUES (?, ?, ?)''', (student_id, subject, marks))
            self.conn.commit()
            print(f"Marks added for student ID {student_id}!")
        else:
            print("Student not found!")

    def generate_log(self):
        self.cursor.execute('''SELECT * FROM students''')
        students = self.cursor.fetchall()
        log = {}
        for student in students:
            student_id = student[0]
            log[student_id] = {
                'name': student[1],
                'age': student[2],
                'contact': student[3],
                'address': student[4],
                'marks': {}
            }
            self.cursor.execute('''SELECT subject, marks FROM marks WHERE student_id = ?''', (student_id,))
            marks = self.cursor.fetchall()
            for subject, mark in marks:
                log[student_id]['marks'][subject] = mark
        with open('transaction_log.txt', 'w') as file:
            for student_id, details in log.items():
                file.write(f"Student ID: {student_id}\n")
                for key, value in details.items():
                    if key != 'marks':
                        file.write(f"  {key.capitalize()}: {value}\n")
                    else:
                        file.write(f"  Marks:\n")
                        for subject, mark in value.items():
                            file.write(f"    {subject}: {mark}\n")
        print("Transaction log generated!")

    def __del__(self):
        self.conn.close()

def main():
    sms = StudentManagementSystem()

    while True:
        print("\n1. Add student")
        print("2. Remove student")
        print("3. View student")
        print("4. View all students")
        print("5. Add marks to student")
        print("6. Generate log")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            student_id = input("Enter student ID: ")
            name = input("Enter name: ")
            age = int(input("Enter age: "))
            contact = input("Enter contact: ")
            address = input("Enter address: ")
            sms.add_student(student_id, name, age, contact, address)
        elif choice == '2':
            student_id = input("Enter student ID: ")
            sms.remove_student(student_id)
        elif choice == '3':
            student_id = input("Enter student ID: ")
            sms.view_student(student_id)
        elif choice == '4':
            sms.view_all_students()
        elif choice == '5':
            student_id = input("Enter student ID: ")
            subject = input("Enter subject: ")
            marks = int(input("Enter marks: "))
            sms.add_student_marks(student_id, subject, marks)
        elif choice == '6':
            sms.generate_log()
        elif choice == '7':
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
