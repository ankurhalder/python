# Definition:
# A pure function is a function that, given the same input, will always produce the same output
# and has no side effects. It depends only on its input parameters.

# Characteristics of Pure Functions:
# 1. Deterministic: Always produces the same result for the same input.
# 2. No Side Effects: Does not modify external state or variables.
# 3. Stateless: Does not depend on the state of external variables.

# Example of a Pure Function:
def add_numbers(x, y):
    return x + y

result = add_numbers(3, 5)
print(result)  # Output: 8

# Examples of Impure Functions (Not Pure Functions):

# 1. Modifying External State:
total = 0

def impure_add_to_total(x):
    global total
    total += x
    return total

result = impure_add_to_total(10)
print(result)  # Output: 10

# 2. Using External State:
external_variable = 5

def impure_multiply_by_external(x):
    return x * external_variable

result = impure_multiply_by_external(3)
print(result)  # Output: 15

# 3. Non-Deterministic:
from random import randint

def impure_random_function(x):
    return x + randint(1, 10)

result = impure_random_function(5)
print(result)  # Output varies on each call

# Benefits of Pure Functions:
# - Easier to Reason: Predictable behavior makes code easier to understand and reason about.
# - Testability: Easy to test because they don't rely on external state.
# - Parallelism: Easier to parallelize since they don't depend on shared state.

# Avoiding Side Effects:
# - Minimize the use of global variables.
# - Avoid modifying mutable objects in place.
# - Favor immutability when possible.

# Example with Immutability:
def pure_add_to_list(lst, value):
    # Creates a new list instead of modifying the input list.
    return lst + [value]

original_list = [1, 2, 3]
new_list = pure_add_to_list(original_list, 4)
print(original_list)  # Output: [1, 2, 3]
print(new_list)       # Output: [1, 2, 3, 4]

# Pure Functions with Immutable Data Structures:
# Immutable data structures help enforce the purity of functions.

from collections import namedtuple

# Using namedtuple for immutability
Person = namedtuple('Person', ['name', 'age'])

def pure_update_person_age(person, new_age):
    return person._replace(age=new_age)

john = Person(name='John', age=25)
updated_john = pure_update_person_age(john, 26)

print(john)         # Output: Person(name='John', age=25)
print(updated_john)  # Output: Person(name='John', age=26)

# Higher-Order Functions:
# Pure functions can take other functions as arguments or return functions.

def pure_operation(func, x, y):
    return func(x, y)

result = pure_operation(add_numbers, 3, 5)
print(result)  # Output: 8

# Conclusion:
# Using pure functions promotes clean, modular, and maintainable code by minimizing side effects
# and improving the predictability of your program.
