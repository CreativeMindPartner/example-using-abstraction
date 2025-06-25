from abc import ABC, abstractmethod

# Abstract class (like a blueprint)
class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

# Concrete class that implements the abstract class
class Car(Vehicle):
    def start(self):
        return "Car engine started! Vroom vroom!"

    def stop(self):
        return "Car engine stopped."

# Using the Car class
my_car = Car()
print(my_car.start())  # Output: Car engine started! Vroom vroom!
print(my_car.stop())   # Output: Car engine stopped.