class Animal: # Create the parent class Animal
    def __init__(self, name): # Initializes the attributes of the Animal class
        # ATTRIBUTES
        self.__name = name # - name (Private)
    # METHODS
    @property # Getter method for name so that it can be accessed by the child classes
    def name(self):
        return self.__name
    def eat(self):
        print(self.__name, "eats food")
    def make_sound(self):
        print(self.__name, "makes a sound")

class Lion(Animal): # Create the child class Lion (that inherits from Animal)
    def __init__(self, name): 
        # ATTRIBUTES
        super().__init__(name) # Calls the constructor of the parent class Animal to initialize name
    # METHODS
    def make_sound(self):
        print(self.name, "roars loudly!")
    def eat(self):
        print(self.name, "eats fresh meat.")

class Elephant(Animal): # Create the child class Elephant (that inherits from Animal)
    def __init__(self, name): 
        # ATTRIBUTES
        super().__init__(name) # Calls the constructor of the parent class Animal to initialize name
    # METHODS    
    def make_sound(self):
        print(self.name, "trumpets!")
    def eat(self):
        print(self.name, "eats grass and fruits.")

class Monkey(Animal): # Create the child class Monkey (that inherits from Animal)
    def __init__(self, name): 
        # ATTRIBUTES
        super().__init__(name) # Calls the constructor of the parent class Animal to initialize name
    # METHODS
    def make_sound(self):
        print(self.name, "chatters!")
    def eat(self):
        print(self.name, "eats bananas.")


# Creating Objects
lion = Lion("Simba")
elephant = Elephant("Dumbo")
monkey = Monkey("George")

lion.make_sound()
lion.eat()
print("-----")

elephant.make_sound()
elephant.eat()
print("-----")

monkey.make_sound()
monkey.eat()
print("-----")