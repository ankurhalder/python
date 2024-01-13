# Step 1
# Define a class called MyFirstClass
class MyFirstClass:
    # Print a message when the class is defined
    print("Who wrote this?")
    
    # Define a class variable
    index = "Author-Book"

    # Step 3
    # Define a function called hand_list() inside the class
    def hand_list(self, philosopher, book):
        # Step 4
        # Print the value of the class variable
        print(MyFirstClass.index)
        
        # Print a formatted string using the passed parameters
        print(philosopher + " wrote the book: " + book)

# Step 5
# Create an instance of the MyFirstClass class
whodunnit = MyFirstClass()

# Call the hand_list method on the created object and pass two values
whodunnit.hand_list("Sun Tzu", "The Art of War")


# Additional Example - Recipe Class
# Define a class called Recipe
class Recipe:
    # Define an initializer method (__init__) to initialize instance variables
    def __init__(self, dish, items, time):
        self.dish = dish
        self.items = items
        self.time = time

    # Define a method called contents to print information about the recipe
    def contents(self):
        print("The " + self.dish + " contains " + str(self.items) + " and takes " + str(self.time) + " to cook")

# Create instances of the Recipe class
# Step 1
# Instantiate an object 'pizza' from the Recipe class with specific parameters
pizza = Recipe("pizza", ["cheese", "dough", "tomato"], 30)

# Instantiate an object 'pasta' from the Recipe class with specific parameters
pasta = Recipe("pasta", ["pasta", "sauce", "cheese"], 20)

# Step 5
# Call the contents method on the 'pizza' object
print(pizza.contents())

# Call the contents method on the 'pasta' object
print(pasta.contents())

# Access instance variables and print them
# Access the 'items' variable of the 'pizza' object
print(pizza.items)

# Access the 'items' variable of the 'pasta' object
print(pasta.items)
