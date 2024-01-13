# Abstract Classes:
# Abstract classes are classes that cannot be instantiated and are meant to be subclassed.
# They often define abstract methods that must be implemented by their subclasses.

from abc import ABC, abstractmethod

# Define an abstract class using ABC (Abstract Base Class) and @abstractmethod decorator.

class Shape(ABC):
    @abstractmethod
    def area(self):
        """Abstract method to calculate the area of the shape."""
        pass

    @abstractmethod
    def perimeter(self):
        """Abstract method to calculate the perimeter of the shape."""
        pass

# Abstract classes provide a common interface for a group of related classes.
# Subclasses must implement all abstract methods defined in the abstract class.

# Concrete Class Implementing Abstract Class:

class Square(Shape):
    def __init__(self, side):
        self.side = side

    # Implement abstract methods area and perimeter.
    def area(self):
        return self.side ** 2

    def perimeter(self):
        return 4 * self.side

# Instantiate the concrete class.
square = Square(5)

# Call the implemented methods.
print("Square Area:", square.area())  # Output: 25
print("Square Perimeter:", square.perimeter())  # Output: 20

# Another Concrete Class Implementing Abstract Class:

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    # Implement abstract methods area and perimeter.
    def area(self):
        return 3.14 * self.radius ** 2

    def perimeter(self):
        return 2 * 3.14 * self.radius

# Instantiate the concrete class.
circle = Circle(3)

# Call the implemented methods.
print("Circle Area:", circle.area())  # Output: 28.26
print("Circle Perimeter:", circle.perimeter())  # Output: 18.84

# More Examples:

# Define another abstract class for vehicles.
class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        """Abstract method to start the vehicle's engine."""
        pass

    @abstractmethod
    def stop_engine(self):
        """Abstract method to stop the vehicle's engine."""
        pass

# Concrete Class Implementing Vehicle:

class Car(Vehicle):
    def start_engine(self):
        return "Car engine started."

    def stop_engine(self):
        return "Car engine stopped."

# Instantiate the concrete class.
car = Car()

# Call the implemented methods.
print("Car Actions:")
print(car.start_engine())  # Output: Car engine started.
print(car.stop_engine())  # Output: Car engine stopped.

# Another Concrete Class Implementing Vehicle:

class Motorcycle(Vehicle):
    def start_engine(self):
        return "Motorcycle engine started."

    def stop_engine(self):
        return "Motorcycle engine stopped."

# Instantiate the concrete class.
motorcycle = Motorcycle()

# Call the implemented methods.
print("\nMotorcycle Actions:")
print(motorcycle.start_engine())  # Output: Motorcycle engine started.
print(motorcycle.stop_engine())  # Output: Motorcycle engine stopped.
