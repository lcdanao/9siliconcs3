# Advanced Class Relationships
## Previous Activities
[Part I - Classes and Objects](classObjectUML.md)<br>
[Part II - Class Attributes and Methods](classAttributesMethods.md)<br>
[Part III - Class Relationships](classRelationships.md)

## Existing System Description:
Class 1: Student<br>
Class 2: Report Card<br>
Problems/Limitations: My current design includes a repeated attribute, specifically the gradeLevel variable, which can create inconsistent data. If a student's grade is updated using the changeGradeLevel method, their existing report cards will still hold old data. 

## Inheritance Relationship
Parent: Student<br>
Child: Olympian<br>
Explanation: An Olympian is a specific type of student who participates in academic olympiads. They inherit all general student attributes like a name, ID number, grade level, and enrollment status, but also possess unique attributes such as a list of specialized subjects and number of medals won.

## Inheritance UML
[Inheritance](images/inheritanceDiagram.png)

## Aggregation
Class containing another object: Olympian<br>
Contained object: Medal<br>
Explanation: An Olympian can earn multiple medals. If an Olympian leaves or is deleted from the system, the Medal objects still exist independently in the school's collection to track the school's overall wins.

## Advanced UML Diagram
[Advanced UML](images/advancedClassDiagram.png)
## Python Implementation
[Source Code](advancedRelationships.py)
## Test Run
[Test](images/advancedTestRun.png)
## Object Diagram
[Object](advancedObjectDiagram.png)

## Reflection
### Why did you choose your inheritance relationship? Explain why your child class is a type of your parent class.
An Olympian is a specialized type of Student, satisfying the "is-a" relationship. They share identical student traits such as having a name, an ID number, and an enrollment status. An Olympian extends this  by having unique traits such as competition records and specialized academic subjects. This  ensures that every Olympian is treated as a student by default while also recognizing their additional characteristics.
### How did inheritance reduce duplicate code? Identify attributes or methods that were reused.
Inheritance stops code repetition by letting the Olympian class reuse everything inside Student. Instead of copy-pasting, the child class inherits the parent class's attributes like name, idNumber, gradeLevel, and enrolled, along with methods such as changeGradeLevel. Olympian only needs to add its own unique fields, like specializedSubjects and medalsWon. This keeps the code organized since updating core student rules only has to be done once in the parent class.
### Why is your HAS-A relationship Composition or Aggregation? Explain the lifecycle relationship between the two objects.
This relationship is classified as Aggregation because the Olympian and the Medal objects have completely independent lifecycles where the part can survive without the whole. Medals are instantiated as independent objects outside of the student profile and passed in as pre-existing references. If an Olympian object is deleted from the school database, the Medal objects remain intact within the system memory as part of the school's historical trophy archive. Because destroying the container does not destroy the contained items, it represents a weak ownership relationship.
### What is the difference between Association from Part III and the advanced relationship you implemented?
The original Association from Part III only had two independent classes simply interact without any structural ownership. In contrast, the newly implemented relationship introduces the "has-a" hierarchy, where one object acts as a container for the other. While association merely lets objects pass data back and forth, aggregation explicitly structures the Olympian as the owner of a medalsWon collection.
### How does your design follow the DRY principle?
The design follows the DRY principle by ensuring every piece of information is stored in only one place. First, inheritance stops us from duplicating core profile code inside the Olympian class. Second, removing gradeLevel from ReportCard ensures a student's grade is tracked only inside the Student object. If a report card needs to display the grade, it reads it directly from the student instead of keeping a separate, duplicate copy.