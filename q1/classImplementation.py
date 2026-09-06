class YourClass:
    def __init__(self, value1, value2, value3):
        self.attribute1 = value1
        self.attribute2 = value2
        self.__private_attribute = value3

    def displayInfo(self):
        print(f"Attribute 1: {self.attribute1}")
        print(f"Attribute 2: {self.attribute2}")
        print(f"Private Attribute: {self.__private_attribute}")