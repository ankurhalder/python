# Taking input as strings
num = input('Please enter a number:')
num2 = input('Please enter another number:')

# Concatenating strings (not performing arithmetic addition)
print("Concatenation (strings):", num + num2)

# Converting input to integers before addition
print("Addition (integers):", int(num) + int(num2))


# Taking input for names
first_name = input('Please enter your first name:')
last_name = input('Please enter your last name:')

# Concatenating strings for a greeting
print('Hello ' + first_name + ' ' + last_name)


# Taking input as floats and performing arithmetic addition
n1 = input('First number is: ')
n2 = input('Second number is: ')
user_sum = float(n1) + float(n2)

# Printing the result after converting inputs to floats
print("The sum of " + str(n1) + " and " + str(n2) + " is " + str(user_sum))
