list1 = [1, 2, 3 ,4 ,5]

list2 = ["A", "B", "C", "D", "E"]

list3 = [1, "A", 2, "B", 3, "C", 4, "D", 5, "E"]

list4 = [[1, "A"], [2, "B"], [3, "C"], [4, "D"], [5, "E"]]

# in the following examples, I have addded data to the list
print(list1)
print(*list1)
list1.insert(len(list1), 10)
print(list1, sep=" ")
list1.append(11)
print(list1, sep=" ")
list1.extend([12, 13, 14])
print(list1, sep=" ")
# in the following examples, I have removed data from the list
list1.pop()
print(list1, sep=" ")
del list1[2]
print(list1, sep=" ")
list1.remove(4)
print(list1, sep=" ")
list1.pop(0)
print(list1, sep=" ")

# in the following examples, I have itarated over the list

for x in list1:
    print(x)