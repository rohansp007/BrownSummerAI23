class Student:
    def __init__(self,name,age,gpa,id,grade):
        self.name = name
        self.age = age
        self.gpa = gpa
        self.id = id
        self.grade = grade
        self.classes = []
    
    def __str__(self):
        print(f'Student Name: {self.name}')
        print(f'Student Age: {self.age}')
        print(f'Student GPA: {self.gpa}')
        print(f'Student ID: {self.id}')
        print(f'Student Grade: {self.grade}')
        print(f"Student's Classes: {self.classes}")
    
    def enrollClass(self,class_enrolled):
        self.classes.append(class_enrolled)
        print(f'Student has successfully enrolled in {class_enrolled}.')
    
    def removeClass(self,class_to_remove):
        if class_to_remove in self.classes:
            self.classes.remove(class_to_remove)
            print(f'Student has successfully dropped out of {class_to_remove}.')
        else:
            print("Student is not enrolled in this course!")
    
    def inClass(self,course):
        if course in self.classes:
            print(f'Student is in {course}.')
        else:
            print(f'Student is not in {course}!')