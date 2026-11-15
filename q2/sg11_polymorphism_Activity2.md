## 1. Answer the following questions:
### a. What is duck typing, as explained in the video?
Duck typing is another way to achieve Polymorphism besides using Inheritance, where an object must only have the minimum necessary attributes and methods, regardless of its original class. Its name comes from its philosophy: "If it looks like a duck and quacks like a duck, it must be a duck."

### b. What did the Car class need to have so it could work inside the same loop as Dog and Cat, even if it does not inherit from the Animal class?
The Car class only required the minimum necessary method (speak) and attribute (alive) to be considered an 'animal', despite not being a part of the Animal class.

## 2. Python Code:

### CODE: [SG11 - Polymorphism Activity 2 Code](sg11_polymorphism_Activity2.py)

## 3. How does the code in 2.2 demonstrate polymorphism?
The code demonstrates polymorphism by allowing different classes with the same method name to perform different behaviors depending on the object it modifies.