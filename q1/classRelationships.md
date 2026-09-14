# Class Relationships: Association and Multiplicity
## Previous Work
[Part I - Classes and Objects](classObjectUML.md)<br>
[Part II - Class Attributes and Methods](classAttributesMethods.md)
## Existing Class
Class: Student<br>
Description: This class represents an individual enrolled at the school. The displayInfo() method outputs student details (name, gradeLevel, idNumber, enrolled) with their grades, while enrollStudent() and changeGradeLevel() ensure the report card matches their current academic status.
## New Related Class
Class: ReportCard<br>
Description: This class represents a transcript/progress document issued quarterly to a student. It manages data such as a student's final GWA. These two classes must be connected because every report card needs to belong to a specific student. Without this link, there would be no way to know whose grades and teacher comments are being recorded.
## Association
Relationship: Student HAS ReportCards<br>
Explanation: This relationship  connects a student's record to their academic documents. It directly links the Student to the official files that hold their grades and teacher feedback.
## Multiplicity
Multiplicity: Student 1 ───────── 0..* ReportCard<br>
Explanation: One Student can have many ReportCards accumulated throughout their academic life to track their grades (e.g., one for each quarter across multiple years). Conversely, each individual ReportCard is unique and can only belong to one specific student to prevent grading mix-ups.
## UML Class Relationship Diagram
![Class Relationship Diagram](images/classRelationshipDiagram.png)
## Python Implementation
[View Python Source](classRelationships.py)
## Test Run
![Relationship Test Run](images/relationshipTestRun.png)
## Object Relationship Diagram
![Object Relationship Diagram](images/objectRelationshipDiagram.png)
## Analysis
### What is the association between your two classes?
This association connects a Student object directly to its corresponding ReportCard objects. It links a student's profile to their quarterly progress, ensuring academic measures like a student's GWA are tied to a verifiable record. By doing this, the system prevents grades and performance data from existing in isolation.
### What multiplicity did you choose and why?
I chose a 1:Many multiplicity because a single student accumulates multiple report cards over a school year. A 1:1 multiplicity would be incorrect because it would restrict a student to only one report card for their entire academic year/life, making it impossible to track separate quarters. Additionally, each individual report card is unique and must belong exclusively to exactly one student to prevent grading mix-ups.
### How did you implement the relationship in Python?
I implemented this relationship in Python by initializing a python list within the Student class constructor. Specifically, the self.reportCards attribute is used to store and manage the collection of related objects. I then created a dedicated method called add_report_card that appends individual ReportCard instances into this list to build the system.
### Why did you store an object reference instead of copying its data?
Storing an object reference allows any live updates made to a report card immediately reflect across the whole system without needing to manually synchronize data. For example, when student1 accesses card1.finalGWA through the list, it reads directly from the original report card. If a teacher modifies that GWA later on, the student object automatically views the updated value since it points to the same object.
### If your relationship uses many, why is a list appropriate?
A list is the most appropriate container for a "many" relationship because it preserves the chronological order of the quarters and allows the collection to grow as new quarters pass. Instead of holding raw data like text strings or numbers, this list actually contains the references of the instantiated ReportCard objects. This structural design allows us to easily loop through the container and call methods or view attributes directly from the connected objects.
