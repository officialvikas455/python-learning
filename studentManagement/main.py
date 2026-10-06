import json
from abc import ABC, abstractmethod
from pathlib import Path

database = "school_data.json"
data = {"student": [], "teacher": []}

# Load existing data safely
if Path(database).exists():
    with open(database, 'r') as f:
        content = f.read()
        if content.strip():
            data = json.loads(content)

def save():
    with open(database, "w") as f:
        json.dump(data, f, indent=4)

class Persons(ABC):
    @abstractmethod
    def get_roles(self):
        pass

    @abstractmethod
    def show_details(self):
        pass

    @abstractmethod
    def register(self):
        pass

    @staticmethod
    def validate_email(email):
        return "@" in email and "." in email
class Student(Persons):
    def get_roles(self):
        return "Student"

    def register(self):
        name = input("Enter your name: ")

        try:
            age = int(input("Enter your age: "))
        except ValueError:
            print("Invalid age entered.")
            return

        email = input("Enter your email: ")
        roll_no = input("Enter your roll no: ")

        if not Persons.validate_email(email):
            print("Invalid email format.")
            return

        for i in data['student']:
            if i["roll_no"] == roll_no:
                print("Student already exists.")
                return

        data['student'].append({
            "name": name,
            "age": age,
            "email": email,
            "roll_no": roll_no,
            "grades": {}
        })
        save()
        print(f"Student {name} registered successfully.")

    def show_details(self):
        pass

class Teacher(Persons):
    def get_roles(self):
        return "teacher"
    def register(self):
        name = input("Enter your name: ")

        try:
            age = int(input("Enter your age: "))
        except ValueError:
            print("Invalid age entered.")
            return
        subject = input("subject")
        emp_id = int(input("Emplotyee id"))

stud = Student()
teac = Teacher()


print("\n--- School Management System ---")
print("1. Register a student")
print("2. Register a teacher")
print("3. Add grades")
print("4. Show student details")
print("5. Show teacher details")

try:
    choice = int(input("Please enter your choice: "))
    if choice == 1:
        stud.register()
    else:
        print("Feature not implemented yet.")
except ValueError:
    print("Please enter a valid number.")
