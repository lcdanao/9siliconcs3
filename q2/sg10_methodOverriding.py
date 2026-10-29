class Animal:
    def __init__(self, name):
        # ATTRIBUTES
        self.__name = name # - name (Private)
    # METHODS
    def eat(self):
        print(self.__name, "eats food")
    def make_sound(self):
        print(self.__name, "makes a sound")

class Lion(Animal):
    def __init__(self, name): 
        # ATTRIBUTES
        super().__init__(name)
    # METHODS
    def make_sound(self):
        print(self.__name, "roars loudly!")
    def eat(self):
        print(self.__name, "eats fresh meat.")

class Elephant(Animal):
    def __init__(self, name): 
        # ATTRIBUTES
        super().__init__(name)
    # METHODS    
    def make_sound(self):
        print(self.__name, "trumpets!")
    def eat(self):
        print(self.__name, "eats grass and fruits.")

class Monkey(Animal):
    def __init__(self, name): 
        # ATTRIBUTES
        super().__init__(name)
    # METHODS
    def make_sound(self):
        print(self.__name, "chatters!")
    def eat(self):
        print(self.__name, "eats bananas.")

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