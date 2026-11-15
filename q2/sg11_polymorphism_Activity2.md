## 1. Answer the following questions:
### a. What is duck typing, as explained in the video?
Duck typing is another way to achieve Polymorphism besides using Inheritance, where an object must only have the minimum necessary attributes and methods, regardless of its original class. Its name comes from its philosophy: "If it looks like a duck and quacks like a duck, it must be a duck."

### b. What did the Car class need to have so it could work inside the same loop as Dog and Cat, even if it does not inherit from the Animal class?
The Car class only required the minimum necessary method (speak) and attribute (alive) to be considered an 'animal', despite not being a part of the Animal class.

## 2. Create the Python code that:
### a. Creates three classes: Car, Boat, and Drone with a method move().
    move() in the Car class prints "The car drives on the road."
    move() in the Boat class prints "The boat sails on water."
    move() in the Drone class prints "The drone flies in the sky."
### b. Has a function named start_trip(vehicle), with a parameter vehicle, that simply calls the move() method: vehicle.move().
### c. Creates one object of each class.
### d. Calls the start_trip() method for each object.

CODE: [Code](sg11_polymorphism_Activity2.py)

## 3. How does the code in 2.2 demonstrate polymorphism?
