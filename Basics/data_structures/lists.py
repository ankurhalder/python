# Creating lists
list1 = [1, 2, 3, 4, 5]
list2 = ["A", "B", "C", "D", "E"]
list3 = [1, "A", 2, "B", 3, "C", 4, "D", 5, "E"]
list4 = [[1, "A"], [2, "B"], [3, "C"], [4, "D"], [5, "E"]]

# Adding elements to a list
list1.insert(len(list1), 10)  # Inserting 10 at the end of list1
list1.append(11)  # Appending 11 at the end of list1
list1.extend([12, 13, 14])  # Extending list1 with [12, 13, 14]

# Removing elements from a list
list1.pop()  # Removing the last element from list1
del list1[2]  # Removing the element at index 2 from list1
list1.remove(4)  # Removing the first occurrence of 4 from list1
list1.pop(0)  # Removing the element at index 0 from list1

# Iterating over a list
for x in list1:
    print(x)

# Output:
# 2
# 3
# 5
# 10
# 11
# 12
# 13

# Printing lists
print(list1)  # Output: [2, 3, 5, 10, 11, 12, 13]
print(*list1)  # Output: 2 3 5 10 11 12 13

# Accessing list elements
print(list1[0])  # Output: 2
print(list2[2])  # Output: C
print(list3[1:6])  # Output: ['A', 2, 'B', 3, 'C']

# Modifying list elements
list1[0] = 1  # Changing the value at index 0 to 1

# Finding the length of a list
length = len(list1)  # Length of list1 is 7

# Checking if an element exists in a list
if 5 in list1:
    print("5 is present in list1")

# Sorting a list
list1.sort()  # Sorting list1 in ascending order
list2.sort(reverse=True)  # Sorting list2 in descending order

# Reversing a list
list3.reverse()  # Reversing the order of elements in list3

# Clearing a list
list4.clear()  # Removing all elements from list4

# Copying a list
list5 = list1.copy()  # Creating a copy of list1

# Finding the index of an element in a list
index = list1.index(5)  # Index of 5 in list1 is 2

# Counting the occurrences of an element in a list
count = list1.count(10)  # Count of 10 in list1 is 1
