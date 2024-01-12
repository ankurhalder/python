def sum_of(*args):
    sum = 0
    for i in args:
        sum += i
    return sum

print(sum_of(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))

def sum_of(*args):
    """
    Calculates the sum of all the numbers passed as arguments.
    
    Args:
        *args: Variable number of arguments.
        
    Returns:
        int: The sum of all the numbers.
    """
    total_sum = 0
    for num in args:
        total_sum += num
    return total_sum

# Example usage
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"The sum of numbers is: {sum_of(*numbers)}")
