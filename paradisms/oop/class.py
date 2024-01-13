class MyClass:
    # Class Variable
    a = 5

    # Instance Method
    def hello(self):
        print("Hello World")

# Creating an Instance of the Class
myc = MyClass()

# Accessing Class Variable
print(myc.a)

# Invoking an Instance Method
myc.hello()


# A good example of a class variable is a constant:
value = 7
class A:
    value = 5
a = A()
a.value = 3
print(value) # 7
print(a.value) # 3
print(A.value) # 5