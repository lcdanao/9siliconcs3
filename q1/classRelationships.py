class ReportCard:
    def __init__(self, name, subjectGrades, finalGWA, gradeLevel):
        self.name = name                 
        self.finalGWA = finalGWA         
        self.gradeLevel = gradeLevel     
        self.__subjectGrades = subjectGrades  

    def displayReportCard(self):
        print(f"--- Report Card: {self.name} ---")
        print(f"Grade Level: {self.gradeLevel}")
        print(f"Subject Grades: {self.__subjectGrades}")
        print(f"Final GWA: {self.finalGWA}")

class Student:
    def __init__(self, name, idNumber, gradeLevel, enrolled):
        self.name = name                 
        self.gradeLevel = gradeLevel     
        self.__idNumber = idNumber       
        self.__enrolled = enrolled       
        self.report_cards = []           

    def add_report_card(self, report_card_reference):
        self.report_cards.append(report_card_reference)

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


student1 = Student("Lee Wonhee", 3252024, 12, True)

card1 = ReportCard("1st Quarter Progress", 91.5, 93.0, 12)
card2 = ReportCard("2nd Quarter Progress", 94.0, 95.2, 12)
card3 = ReportCard("3rd Quarter Progress", 92.5, 93.8, 12)

student1.add_report_card(card1)
student1.add_report_card(card2)
student1.add_report_card(card3)

print(f"Accessing report card data through {student1.name}'s object system:\n")

for card in student1.report_cards:
    print(f"Report Card Name: {card.name} | Final GWA: {card.finalGWA}")
