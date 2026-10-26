class Animal:

class Lion(Animal):

class Elephant(Animal):

class Monkey(Animal):


lion = Lion("Simba")
elephant = Elephant("Dumbo")
monkey = Monkey("George")

print(lion.make_sound())
print(lion.feed())
print("-----")
print(elephant.make_sound())
print(elephant.feed())
print("-----")
print(monkey.make_sound())
print(monkey.feed())
print("-----")