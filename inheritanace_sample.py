class Person:
    def __init__(self, pid, name, age, ):
        self.pid = pid
        self.name = name
        self.age = age
        
class Student(Person):
    def __init__(self, pid, name, age, student_id, ):
        super().__init__(pid, name, age,)
        self.student_id = student_id

class Staff(Person):
    def __init__(self, pid, name, age, staff_id,):
        super().__init__(pid, name, age)
        self.staff_id = staff_id


    

student = Student(1, "Alice", 20, "S12345")
staff = Staff(2, "Bob", 35, "ST54321")
print(f"Student: {student.name}, Age: {student.age}, Student ID: {student.student_id}")
print(f"Staff: {staff.name}, Age: {staff.age}, Staff ID: {staff.staff_id}")