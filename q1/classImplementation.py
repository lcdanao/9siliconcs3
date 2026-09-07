class Student:
    def __init__(self, name, idNumber, gradeLevel, enrolled):
        # ATTRIBUTES 
        self.name = name # + name (Public)
        self.gradeLevel = gradeLevel # + gradeLevel (Public)
        self.__idNumber = idNumber # - idNumber (Private)
        self.__enrolled = enrolled # - enrolled (Private)

    # METHODS
    def displayInfo(self):
        print(f"Name: {self.name}")
        print(f"Grade Level: {self.gradeLevel}")
        print(f"ID Number: {self.__idNumber}")
        print(f"Enrollment Status: {'Enrolled' if self.__enrolled else 'Not Enrolled'}")

    def enrollStudent(self):
        if not self.__enrolled:
            self.__enrolled = True
            print(f"{self.name} has been successfully enrolled!")
        else:
            print(f"{self.name} is already enrolled.")

    def changeGradeLevel(self, newGrade):
        if 7 <= newGrade <= 12:
            self.gradeLevel = newGrade
            print(f"Grade level updated to {self.gradeLevel}.")
        else:
            print("Invalid grade level. Please enter a grade between 7 and 12.")

class Student:
    def __init__(self, name, idNumber, gradeLevel, enrolled):
        # Public attributes
        self.name = name
        self.gradeLevel = gradeLevel
        
        # Private attributes
        self.__idNumber = idNumber
        self.__enrolled = enrolled

# TEST RUN
if __name__ == "__main__":
    # Create the two student objects from your diagram
    student1 = Student(name="Lee Wonhee", idNumber=3252024, gradeLevel=12, enrolled=True)
    student2 = Student(name="Kim Juhoon", idNumber=8182025, gradeLevel=11, enrolled=True)

    print("--- BEFORE ---")
    print("Object 1:")
    student1.displayinfo()
    print("Object 2:")
    student2.displayinfo()

    print("\nPerforming action on Object 1...")
    student1.changeGradeLevel(11) 

    print("\n--- AFTER ---")
    print("Object 1:")
    student1.displayinfo()
    print("Object 2:")
    student2.displayinfo()

