def sum_of(**kwargs):
    sum = 0
    for i,j in kwargs.items():
        sum += j
    return sum

print(sum_of (a=1, b=2, c=3, d=4, e=5, f=6, g=7, h=8, i=9, j=10))

def greet(**kwargs):
    # The greet function takes in keyword arguments using the **kwargs syntax.
    # This allows us to pass any number of keyword arguments to the function.

    for key, value in kwargs.items():
        # The items() method returns a view object that contains the key-value pairs of the dictionary.
        # In this case, kwargs is a dictionary containing the keyword arguments passed to the function.

        print(f"{key} : {value}")
        # We iterate over each key-value pair in kwargs and print them in the format "key : value".
        # This will display the name and value of each keyword argument passed to the function.

greet(name="Alice", age=25)
# We call the greet function and pass two keyword arguments: name="Alice" and age=25.
# The function will print "name : Alice" and "age : 25" as output.