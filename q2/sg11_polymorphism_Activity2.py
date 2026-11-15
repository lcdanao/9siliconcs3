class Car:
    def move(self):
        print("The car drives on the road.")

class Boat:
    def move(self):
        print("The boat sails on water.")

class Drone:
    def move(self):
        print("The drone flies in the sky.")

def start_trip(vehicle):
    vehicle.move()

# Creating Objects
car = Car()
boat = Boat()
drone = Drone()

# Call the start_trip() method for each object
start_trip(car)
start_trip(boat)
start_trip(drone)