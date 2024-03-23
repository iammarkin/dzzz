class Student:
    def __init__(self, name, age, year, grade):
        self.name = name
        self.age = age
        self.year = year
        self.grade = grade

    def get_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Year: {self.year}")
        print(f"Grade: {self.grade}")

    def increase_year(self):
        self.year += 1

    def update_grade(self, new_grade):
        self.grade = (self.grade + new_grade) / 2


student1 = Student("John", 20, 2, 85)
student2 = Student("Alice", 21, 3, 90)

print("Student 1 information:")
student1.get_info()
print()

print("Student 2 information:")
student2.get_info()
print()

student1.increase_year()
print("After increasing year for student 1:")
student1.get_info()
print()

student2.update_grade(95)
print("After updating grade for student 2:")
student2.get_info()