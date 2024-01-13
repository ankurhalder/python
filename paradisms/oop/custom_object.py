# Step 1
# Define a class called MyFirstClass
class MyFirstClass:
    # Step 2
    # Print a message when the class is defined
    print("Who wrote this?")

    # Step 3
    # Define a class variable
    index = "Author-Book"

    # Step 4
    # Define a function called hand_list() inside the class
    def hand_list(self, philosopher, book):
        # Step 5
        # Print the value of the class variable
        print(MyFirstClass.index)

        # Print a formatted string using the passed parameters
        print(philosopher + " wrote the book: " + book)

# Step 6
# Create an instance of the MyFirstClass class
whodunnit = MyFirstClass()

# Step 7
# Call the hand_list method on the created object and pass two values
whodunnit.hand_list("Sun Tzu", "The Art of War")

# Additional Example - Recipe Class
# Define a class called Recipe
class Recipe:
    # Step 1
    # Define an initializer method (__init__) to initialize instance variables
    def __init__(self, dish, items, time):
        self.dish = dish
        self.items = items
        self.time = time

    # Step 2
    # Define a method called contents to print information about the recipe
    def contents(self):
        print("The " + self.dish + " contains " + str(self.items) + " and takes " + str(self.time) + " to cook")

# Step 3
# Create instances of the Recipe class

# Step 4
# Instantiate an object 'pizza' from the Recipe class with specific parameters
pizza = Recipe("pizza", ["cheese", "dough", "tomato"], 30)

# Step 5
# Instantiate an object 'pasta' from the Recipe class with specific parameters
pasta = Recipe("pasta", ["pasta", "sauce", "cheese"], 20)

# Step 6
# Call the contents method on the 'pizza' object
print("Pizza Recipe:")
pizza.contents()

# Step 7
# Call the contents method on the 'pasta' object
print("\nPasta Recipe:")
pasta.contents()

# Step 8
# Access instance variables and print them

# Step 9
# Access the 'items' variable of the 'pizza' object
print("\nIngredients for Pizza:")
print(pizza.items)

# Step 10
# Access the 'items' variable of the 'pasta' object
print("\nIngredients for Pasta:")
print(pasta.items)
