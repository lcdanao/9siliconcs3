# Class Attributes and Methods
## Previous Design
Link to my previous activity:
[classObjectUML.md](classObjectUML.md)
## Design Revision
No major changes were needed from my original design.
## Visibility Decisions
| Attribute | Data Type | Visibility | Reason |
|---|---|---|---|
| name | string | Public | Easy to view and change directly because it is safe and used often. |
| idNumber | int | Private | A sensitive identifier that should remain private to prevent accidental modification. |
| gradeLevel | int | Public | Commonly updated and read by external classes, such as class lists. |
| enrolled | boolean | Private | The system must check criteria (e.g., paid tuition or complete clearance) before enrollment status can change. |
## Updated UML Class Diagram
![Class Diagram](images/classDiagramSG5.png)
## Python Implementation
[View Python Source](classImplementation.py)
## Test Run
![Test Run](images/classTestRun.png)
## Object Diagram
![Object Diagram](images/objectDiagram.png)
## Analysis
### Why did you make your chosen attribute private?
I made the attributes idNumber and enrolled private because they hold sensitive identification and registration records. If outside parts of the program could change them directly, an ID number could accidentally be duplicated or tampered with, corrupting the student database. Similarly, someone could flip the enrollment status without checking if the student actually paid their tuition or submitted papers. Restricting direct access ensures these values can only be updated through secure, pre-approved rules.
### Which method changes the state of your object?

### How did your two objects demonstrate that instances are independent?

### What is the difference between your class diagram and your object diagram?
The class diagram acts as a blueprint or template that defines what a generic student has/is. It lists the structure, showing variable names and data types, such as name : string, without any real identities. In contrast, the object diagram includes actual, real-world data built from that blueprint. It fills the template with specific information, such as the names 'Lee Wonhee' and 'Kim Juhoon', along with their other information.