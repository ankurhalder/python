# Class Definition
class MyClass:
    # Class Variable
    class_variable = 10

    # Constructor (Initializer Method)
    def __init__(self, instance_variable):
        """
        Constructor method to initialize an instance of the class.
        :param instance_variable: Value to set for the instance variable.
        """
        # Instance Variables
        self.instance_variable = instance_variable
        self.__private_variable = "I am private"

    # Instance Method
    def hello(self):
        """
        Instance method to print a greeting.
        """
        print("Hello World!")

    # Getter Method
    def get_private_variable(self):
        """
        Getter method to retrieve the value of the private variable.
        :return: The value of the private variable.
        """
        return self.__private_variable

    # Setter Method
    def set_private_variable(self, new_value):
        """
        Setter method to modify the value of the private variable.
        :param new_value: New value for the private variable.
        """
        self.__private_variable = new_value

    # Class Method
    @classmethod
    def class_method(cls):
        """
        Class method to print information about the class.
        """
        print(f"I am a class method. Class Variable: {cls.class_variable}")

    # Static Method
    @staticmethod
    def static_method():
        """
        Static method that does not depend on class or instance variables.
        """
        print("I am a static method")

    # Magic Method (dunder method)
    def __str__(self):
        """
        Magic method to define the string representation of the object.
        :return: String representation of the object.
        """
        return f"MyClass instance with instance_variable: {self.instance_variable}"

# Creating Instances of the Class
obj1 = MyClass(instance_variable="Object 1")
obj2 = MyClass(instance_variable="Object 2")

# Accessing Class Variable
print(obj1.class_variable)  
# Class Variable: A variable shared among all instances of the class.
# Explanation: Accessed using the instance or the class name.

# Accessing and Modifying Instance Variables
print(obj1.instance_variable)  
# Instance Variables: Variables that belong to an instance of the class.
# Explanation: Accessed and modified using the instance name.

# Accessing Private Variable using Getter Method
print(obj1.get_private_variable())  
# Getter Method: Method to retrieve the value of a private variable.
# Explanation: Ensures controlled access to private variables.

# Modifying Private Variable using Setter Method
obj1.set_private_variable("New private value")
print(obj1.get_private_variable())  
# Setter Method: Method to modify the value of a private variable.
# Explanation: Ensures controlled modification of private variables.

# Invoking Instance Method
obj1.hello()  
# Instance Method: A method that operates on an instance of the class.
# Explanation: Called using the instance name and can access instance variables.

# Invoking Class Method
MyClass.class_method()  
# Class Method: A method that operates on the class itself.
# Explanation: Decorated with @classmethod, can access and modify class variables.

# Invoking Static Method
MyClass.static_method()  
# Static Method: A method that does not depend on class or instance variables.
# Explanation: Decorated with @staticmethod, operates independently.

# Using the Magic Method (__str__)
print(obj1)  
# Magic Method (__str__): A special method for defining the string representation of an object.
# Explanation: Automatically called when using the str() function, facilitates custom object representation.
