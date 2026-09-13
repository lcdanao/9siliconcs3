class ReportCard:
    def __init__(self, name, finalGWA, gradeLevel):
        # ATTRIBUTES
        self.name = name # + name (Public)
        self.finalGWA = finalGWA # + finalGWA (Public)
        self.gradeLevel = gradeLevel # + gradeLevel (Public)
    # METHODS
    def displayReportCard(self):
        print(f"Report Card Name: {self.name} | Final GWA: {self.finalGWA}")

class Student:
    def __init__(self, name, idNumber, gradeLevel, enrolled):
        # ATTRIBUTES
        self.name = name # + name (Public)
        self.gradeLevel = gradeLevel # + gradeLevel (Public)
        self.__idNumber = idNumber # - idNumber (Private)
        self.__enrolled = enrolled # - enrolled (Private)
        self.reportCards = [] # + reportCards (Public)

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
        
    def add_report_card(self, reportCardReference):
            self.reportCards.append(reportCardReference)
    
print("--- BEFORE RELATIONSHIP ---")
student1 = Student("Lee Wonhee", 3252024, 12, True)
card1 = ReportCard("1st Quarter", 94.0, 12)
card2 = ReportCard("2nd Quarter", 96.2, 12)
card3 = ReportCard("3rd Quarter", 95.8, 12)

student1.displayInfo()
print(f"Available report cards to link: {len([card1, card2, card3])} records pending assignment.")
print(f"Student's current linked report card count: {len(student1.reportCards)}")

print("\n--- BUILDING RELATIONSHIP ---")
print("Adding/assigning related objects...")
student1.add_report_card(card1)
print(f"Successfully linked: {card1.name}")
student1.add_report_card(card2)
print(f"Successfully linked: {card2.name}")
student1.add_report_card(card3)
print(f"Successfully linked: {card3.name}")

print("\n--- AFTER RELATIONSHIP ---")
student1.displayInfo()
print(f"Student's current linked report card count: {len(student1.reportCards)}")

print("\nRelated object(s):")
for card in student1.reportCards:
    card.displayReportCard()
