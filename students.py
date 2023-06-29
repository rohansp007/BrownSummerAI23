class Student:
    def __init__(self,name,age,gpa,id,grade):
        self.name = name
        self.age = age
        self.gpa = gpa
        self.id = id
        self.grade = grade
        self.classes = []
    
    def __str__(self):
        print(f'{self.name}' + "'s " f'Name: {self.name}')
        print(f'{self.name}' + "'s " f'Age: {self.age}')
        print(f'{self.name}' + "'s " f'GPA: {self.gpa}')
        print(f'{self.name}' + "'s " f'ID: {self.id}')
        print(f'{self.name}' + "'s " f'Grade: {self.grade}')
        print(f'{self.name}' + "'s " f'Classes: {self.classes}')
    
    def enrollClass(self,class_enrolled):
        self.classes.append(class_enrolled)
        print(f'{self.name} has successfully enrolled in {class_enrolled}.')
    
    def removeClass(self,class_to_remove):
        if class_to_remove in self.classes:
            self.classes.remove(class_to_remove)
            print(f'{self.name} has successfully dropped out of {class_to_remove}.')
        else:
            print(f"{self.name} is not enrolled in {class_to_remove}!")
    
    def inClass(self,course):
        if course in self.classes:
            print(f'{self.name} is in {course}.')
        else:
            print(f'{self.name} is not in {course}!')
