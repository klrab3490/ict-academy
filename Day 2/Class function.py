# Evening Session: Day 1(Part A)

'''
Object For Student
	5 attribule Reg, name m1,m2,m3

input how many students: n
add students to disctionary register number as key: name
'''

class Student:
    student_dict = {}  # Class-level dictionary to store student data

    def __init__(self, num, name, m1, m2, m3):
        self.reg_number = num
        self.name = name
        self.mark1 = m1
        self.mark2 = m2
        self.mark3 = m3
        
    def add_to_dict(self):
        # Add student to dictionary with reg_number as key
        Student.student_dict[self.reg_number] = {
            "name": self.name,
            "marks": {
                "mark1": self.mark1,
                "mark2": self.mark2,
                "mark3": self.mark3
            }
        }
        
    @classmethod
    def display_students(cls):
        # Display all students stored in the dictionary
        for reg_number, data in cls.student_dict.items():
            print(f"Reg Number: {reg_number}, Name: {data['name']}, Marks: {data['marks']}")

# Create an instance of Student
s1 = Student(221039, "Rahul", 50, 50, 50)
s1.add_to_dict()  # Add Rahul to the dictionary

s2 = Student(221040, "Ajith", 60, 70, 80)
s2.add_to_dict()  # Add Anjali to the dictionary

# Display all students in the dictionary
Student.display_students()
