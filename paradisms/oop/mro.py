# Methods and Method Resolution Order (MRO)

# Example 1
class A:
    def a(self):
        return "Function inside A"

class B:
    def a(self):
        return "Function inside B"

# Multiple inheritance: Class C inherits from classes B and A
class C(B, A):
    pass

# Driver code
c = C()
print(c.a())  # Output: Function inside B
# Explanation: Class C inherits from B and A. When searching for method 'a', it follows the order B -> A.

# Example 2
class A:
    def b(self):
        return "Function inside A"

class B:
    def b(self):
        return "Function inside B"

# Multiple inheritance: Class C inherits from classes A and B
class C(A, B):
    pass

# Class D inherits from C
class D(C):
    pass

d = D()
print(d.b())  # Output: Function inside C
# Explanation: Class D accesses the immediate superclass of C, which is A. If not found, it searches B.

# Example 3
class A:
    def c(self):
        return "Function inside A"

# Multiple inheritance: Class C inherits from classes B and A
class C(B, A):
    pass

# Class D inherits from C
class D(C):
    pass

d = D()
# Uncomment the line below to avoid error
# print(d.a)  # Output: AttributeError: 'D' object has no attribute 'a'
# Explanation: In case of ambiguity, Python raises an error because it cannot determine which method to use.

# Example 4
class A:
    def d(self):
        return "Function inside A"

class B:
    def d(self):
        return "Function inside B"

class C:
    def d(self):
        return "Function inside C"

# Multiple inheritance: Class D inherits from A, B, and C
class D(A, B):
    def d(self):
        return "Function inside D"

class E(B, C):
    def d(self):
        return "Function inside E"

# Multiple inheritance: Class F inherits from E, D, and C
class F(E, D, C):
    pass

f = F()
print(f.d())  # Output: Function inside E
print(F.mro())  # Output: Method Resolution Order for class F
# Explanation: Class F directly inherits from its immediate superclass and the first class passed to it.

# Example 5
class A:
    def b(self):
        return "Function inside A"

class B:
    pass

class C:
    def b(self):
        return "Function inside C"

# Uncomment the lines below to avoid error
# class D(B, C, A):
#     pass
# d = D()
# print(d.b())  # Output: AttributeError: 'D' object has no attribute 'b'
# Explanation: It raises an error as the order of inheritance cannot be resolved consistently.

# Example 6
class A:
    pass

class B(A):
    pass

class C(B):
    pass

c = C()
# Uncomment the line below to avoid error
# print(c.a())  # Output: AttributeError: 'C' object has no attribute 'a'
# Explanation: Since no method 'a' is defined in C or its superclasses, it raises an attribute error.
