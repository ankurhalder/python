favorite_fruits = ["apple", "banana", "orange", "grape", "mango"]
# for loop
for i in range(10):
    print("looping for the ", i, "th time")
    
for items in favorite_fruits:
    print(items)
    
# while loop
count = 0

while count <len(favorite_fruits):
    print(favorite_fruits[count])
    # count += 1