
# Independent Object Class (Aggregation)
class Medal:
    def __init__(self, color: str, year: int, subject: str):
        self.color = color      # e.g., "Gold", "Silver"
        self.year = year
        self.subject = subject

    def displayMedal(self):
        print(f"   - [{self.year}] {self.color} Medal in {self.subject}")


class ReportCard:
    def __init__(self, quarter, finalGWA):
        # ATTRIBUTES
        self.quarter = quarter 
        self.finalGWA = finalGWA 
    # METHODS
    def displayReportCard(self):
        print(f"Report Card Quarter: {self.quarter} | Final GWA: {self.finalGWA}")

# Parent Class
class Student:
    def __init__(self, name, idNumber, gradeLevel, enrolled):
        # ATTRIBUTES
        self.name = name # + name (Public)
        self.gradeLevel = gradeLevel # + gradeLevel (Public)
        self.__idNumber = idNumber # - idNumber (Private)
        self.__enrolled = enrolled # - enrolled (Private)
        self.reportCards = [] # + reportCards (Public)
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
        
    def add_report_card(self, reportCardReference):
        self.reportCards.append(reportCardReference)

# Child Class
class Olympian(Student):
    def __init__(self, name, idNumber, gradeLevel, enrolled, specializedSubjects):
        super().__init__(name, idNumber, gradeLevel, enrolled)
        
        # ADDITIONAL ATTRIBUTES
        self.specializedSubjects = specializedSubjects # + specializedSubjects (Public)
        self.medalsWon = [] # + medalsWon (Public)

    # AGGREGATION
    def earnMedal(self, medal):
        self.medalsWon.append(medal)
        print(f"{self.name} won a {medal.color} medal!")

    # ADDITIONAL METHODS
    def displayOlympianInfo(self):
        self.displayInfo()
        print(f"Specialized Subjects: {self.specializedSubjects}")
        
        print("Linked Report Cards:")
        if not self.reportCards:
            print("   (No report cards linked)")
        for card in self.reportCards:
            card.displayReportCard()

        print("Medals Awarded:")
        if not self.medalsWon:
            print("   (No medals won yet)")
        for medal in self.medalsWon:
            medal.displayMedal()

if __name__ == "__main__":
    print("--- 1. PRE-EXISTING OBJECT CREATION (AGGREGATION BASE) ---")
    olympiad_gold = Medal("Gold", 2026, "Mathematics")
    print("Medal created in system database registry.")

    print("\n--- 2. OBJECT INSTANTIATION WITH INHERITANCE ---")
    olympian1 = Olympian("Lee Wonhee", 3252024, 12, True, "Calculus & Physics")
    card1 = ReportCard("1st", 94.0)
    card2 = ReportCard("2nd", 96.2)
    
    olympian1.add_report_card(card1)
    olympian1.add_report_card(card2)

    print("\n--- 3. CONNECTING VIA AGGREGATION ---")
    olympian1.earnMedal(olympiad_gold)
    
    print("\n--- 4. FULL STUDENT PORTFOLIO ---")
    olympian1.displayOlympianInfo()
    