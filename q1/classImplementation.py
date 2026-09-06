class Student:
    def __init__(self, name, idNumber, gradeLevel, enrolled):
        # Public attributes
        self.name = name
        self.gradeLevel = gradeLevel
        
        # Private attributes 
        self.__idNumber = idNumber
        self.__enrolled = enrolled

    def displayInfo(self):
        print(f"Name: {self.name}")
        print(f"Grade Level: {self.gradeLevel}")
        print(f"ID Number: {self.__idNumber}")
        print(f"Enrollment Status: {'Enrolled' if self.__enrolled else 'Not Enrolled'}")