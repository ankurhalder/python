# Create an empty set
my_set = set()

# Add elements to the set
my_set.add(1)
my_set.add(2)
my_set.add(3)

# Print the set
print("Set:", my_set)

# Check if an element is present in the set
print("Is 2 present in the set?", 2 in my_set)

# Remove an element from the set
my_set.remove(2)
print("Set after removing 2:", my_set)

# Get the length of the set
print("Length of the set:", len(my_set))

# Create a set with initial elements
my_set2 = {3, 4, 5}

# Union of two sets
union_set = my_set.union(my_set2)
print("Union of two sets:", union_set)

# Intersection of two sets
intersection_set = my_set.intersection(my_set2)
print("Intersection of two sets:", intersection_set)

# Difference between two sets
difference_set = my_set.difference(my_set2)
print("Difference between two sets:", difference_set)

# Symmetric difference between two sets
symmetric_difference_set = my_set.symmetric_difference(my_set2)
print("Symmetric difference between two sets:", symmetric_difference_set)

# Check if a set is a subset of another set
subset_check = my_set.issubset(my_set2)
print("Is my_set a subset of my_set2?", subset_check)

# Check if a set is a superset of another set
superset_check = my_set.issuperset(my_set2)
print("Is my_set a superset of my_set2?", superset_check)

# Check if two sets are disjoint
disjoint_check = my_set.isdisjoint(my_set2)
print("Are my_set and my_set2 disjoint?", disjoint_check)

# Copy a set
my_set_copy = my_set.copy()
print("Copy of my_set:", my_set_copy)

# Remove and return an arbitrary element from the set
arbitrary_element = my_set.pop()
print("Arbitrary element removed from my_set:", arbitrary_element)

# Clear all elements from the set
my_set.clear()
print("Set after clearing all elements:", my_set)
