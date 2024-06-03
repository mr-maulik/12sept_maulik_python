import json

class StudentManagementSystem:
    def __init__(self):
        self.students = {}

    def add_student(self, student_id, name, age, contact, address):
        if student_id in self.students:
            print(f"Student ID {student_id} already exists!")
        else:
            self.students[student_id] = {
                'name': name,
                'age': age,
                'contact': contact,
                'address': address
            }
            print(f"Student {name} added successfully!")

    def remove_student(self, student_id):
        if student_id in self.students:
            del self.students[student_id]
            print(f"Student ID {student_id} removed successfully!")
        else:
            print("Student not found!")

    def view_student(self, student_id):
        if student_id in self.students:
            print(f"Student ID: {student_id}")
            for key, value in self.students[student_id].items():
                if key != 'marks':
                    print(f"{key.capitalize()}: {value}")
                else:
                    print("Marks:")
                    for subject, marks in value.items():
                        print(f"  {subject}: {marks}")
        else:
            print("Student not found!")

    def view_all_students(self):
        if not self.students:
            print("No students available.")
        else:
            for student_id, details in self.students.items():
                print(f"\nStudent ID: {student_id}")
                for key, value in details.items():
                    if key != 'marks':
                        print(f"{key.capitalize()}: {value}")
                    else:
                        print("Marks:")
                        for subject, marks in value.items():
                            print(f"  {subject}: {marks}")

    def add_student_marks(self, student_id, subject, marks):
        if student_id in self.students:
            if 'marks' not in self.students[student_id]:
                self.students[student_id]['marks'] = {}
            self.students[student_id]['marks'][subject] = marks
            print(f"Marks added for student ID {student_id}!")
        else:
            print("Student not found!")

    def generate_log(self):
        with open('transaction_log.json', 'w') as file:
            json.dump(self.students, file, indent=4)
        print("Transaction log generated!")

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
            print("Invalid choice! Please try again.")y

if __name__ == "__main__":
    main()
