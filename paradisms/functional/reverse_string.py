# using slice function
trial = "reverse_string"
new_trial = trial[::-1] 
print(new_trial)

# using slice (recursion) function 
def reverse_string(string):
    if len(string) == 0:
        return string
    else:
        return reverse_string(string[1:]) + string[0]
print(reverse_string("reverse_string"))