# Simple Inheritance:
# Define a base class A.
class A:
    pass

# Define a class B inheriting from class A.
class B(A):
    pass

# Multiple Inheritance:
# Define class A with attribute 'a'.
class A:
    a = 1

# Define class B with attribute 'b'.
class B:
    b = 2

# Define class C inheriting from both A and B.
class C(A, B):
    pass

# Create an instance of C and print attributes from A and B.
c = C()
print(c.a, c.b)  # Output: 1 2

# Multi-level Inheritance:
# Define class A with attribute 'a'.
class A:
    a = 1

# Define class B inheriting from A and overriding 'a'.
class B(A):
    a = 2

# Define class C inheriting from B.
class C(B):
    pass

# Create an instance of C and print attribute 'a'.
c = C()
print(c.a)  # Output: 2

# Built-in Functions:

# issubclass():
# Check if B is a subclass of A and vice versa.
print(issubclass(B, A))  # Output: False
print(issubclass(A, B))  # Output: True

# isinstance():
# Create an instance b of class B and check its types.
b = B()
print(isinstance(b, B))  # Output: True
print(isinstance(b, A))  # Output: False

# super() Function:
# Define a base class Fruit.
class Fruit:
    def __init__(self, fruit):
        print('Fruit type: ', fruit)

# Define a class FruitFlavour inheriting from Fruit.
class FruitFlavour(Fruit):
    def __init__(self):
        # Call the parent class constructor using super().
        super().__init__('Apple')
        print('Apple is sweet')

# Create an instance of FruitFlavour.
apple = FruitFlavour()
# Output:
# Fruit type:  Apple
# Apple is sweet

# Exploration Exercise:

# Class A definition with constructor and a method.
class A:
    def __init__(self, c):
        print("---------Inside class A----------")
        self.c = c
    print("Print inside A.")

    def alpha(self):
        c = self.c + 1
        return c

# Print the attributes and methods of class A using dir().
print(dir(A))  # Output: ['__init__', 'alpha', '__doc__', '__module__', '__weakref__']

# Instantiate A with a value for c.
print("Instantiating A..")
a = A(1)
print(a.alpha())  # Output: 2

# Class B definition inheriting from A.
class B:
    def __init__(self, a):
        print("---------Inside class B----------")
        self.a = a

    # Uncommenting this line would result in an error, as 'a' is not defined here.
    # print(a.alpha())
    
    # Define a class variable 'd'.
    d = 5
    print(d)
    
    # Uncommenting this line would result in an error, as 'a' is not defined here.
    # print(a)

# Instantiate B with object a from class A.
print("Instantiating B..")
b = B(a)
# Output:
# Hello World!
# Print inside A.
# ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__',
#  '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__',
#  '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__',
#  '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__',
#  'alpha']
# Instantiating A..
# ---------Inside class A----------
# 2
# 5
# <submission.A object at 0x7fcab3ef6940>
# Instantiating B..

# Employee and Supervisor Example:
# Define a base class Employee with name and last attributes.
class Employee:
    def __init__(self, name, last):
        self.name = name
        self.last = last

# Define a class Supervisor inheriting from Employee with an additional password attribute.
class Supervisor(Employee):
    def __init__(self, name, last, password):
        super().__init__(name, last)
        self.password = password

# Define a class Chef inheriting from Employee with a leave_request method.
class Chef(Employee):
    def leave_request(self, days):
        return "May I take a leave for " + str(days) + " days"

# Instantiate objects of Employee, Supervisor, and Chef.
adrian = Employee("Adrian", "A")
juno = Chef("Juno", "J")
ankur = Supervisor("Ankur", "A", "1234")

# Print attributes and methods of objects.
print(ankur.password)  # Output: 1234
print(juno.leave_request(5))  # Output: May I take a leave for 5 days
print(adrian.name)  # Output: Adrian
