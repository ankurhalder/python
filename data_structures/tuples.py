my_tuples = ("hi" , 1 , 4.5 , True , [1, 2, 3] , (1, 2, 3) , {"a": 1, "b": 2, "c": 3})

print(type(my_tuples))
print(my_tuples.count("hi"))
print(my_tuples.index([1,2,3]))

for x in my_tuples:
    print(x)
    
# touple can not be changed in any way