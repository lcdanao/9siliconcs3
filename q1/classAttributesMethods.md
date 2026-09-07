# Class Attributes and Methods
## Previous Design
Link to my previous activity:
[classObjectUML.md](classObjectUML.md)
## Design Revision
No major changes were needed from my original design.
## Visibility Decisions
| Attribute | Data Type | Visibility | Reason |
|---|---|---|---|
| name | string | Public | It is easy to view and change directly because it is safe and used often. |
| idNumber | int | Private | A sensitive identifier that should remain private to prevent accidental modification. |
| gradeLevel | int | Public | It is commonly updated and read by external classes, such as class lists. |
| enrolled | boolean | Private | The system must check criteria (e.g., paid tuition or complete clearance) before enrollment status can change. |
## Updated UML Class Diagram
![Class Diagram](images/classDiagramSG5.png)
## Python Implementation
### [View Python Source](classImplementation.py)
## Test Run
![Test Run](images/TestRun.png)
## Object Diagram
![Object Diagram](images/objectDiagram.png)
## Analysis
### Why did you make your chosen attribute private?
I made the attributes idNumber and enrolled private because they hold sensitive identification and registration records. If outside parts of the program could change them directly, an ID number could accidentally be duplicated or tampered with, corrupting the student database. Similarly, someone could flip the enrollment status without checking if the student actually paid their tuition or submitted papers. Restricting direct access ensures these values can only be updated through secure, pre-approved rules.
### Which method changes the state of your object?
The changeGradeLevel method directly changes the state of my student object. It is applied to the gradeLevel attribute by receiving a new number from the user as a parameter. Before applying the change, the method checks to make sure the input falls between grade 7 and grade 12. If the number is valid, it replaces the old grade level with the new one and prints a success message.
### How did your two objects demonstrate that instances are independent?
The test run's output proves that instances are completely independent because changing one student did not affect the other. When the action was called to modify student1, only their specific data fields were updated in memory. The final print showed that student2 kept their original, unchanged values. This demonstrates that even though both objects share the same layout, they hold completely separate, independent data.
### What is the difference between your class diagram and your object diagram?
The class diagram acts as a blueprint or template that defines what a generic student has/is. It lists the structure, showing variable names and data types, such as name : string, without any real identities. In contrast, the object diagram includes actual, real-world data built from that blueprint. It fills the template with specific information, such as the names 'Lee Wonhee' and 'Kim Juhoon', along with their other information.