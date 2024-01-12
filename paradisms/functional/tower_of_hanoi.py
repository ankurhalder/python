# Introduction
# The Tower of Hanoi is a popular puzzle in mathematics and programming.
# It's widely considered as a good way to demonstrate recursion.
# There is a legend about an ancient Hindu temple containing a large room with three posts surrounded by 64 golden disks.
# The puzzle was presented to a young priest who was told to move all the disks from one post to another without violating a set of given rules.
# By estimates, if the priest followed the rules and moved one disk per second, the puzzle would be solved in 2^64 – 1 seconds.
# That's about 585 billion years. By then the temple would no longer exist.
# Inspired by this legend, a French mathematician Edouard Lucas invented the Tower of Hanoi puzzle more than a hundred years ago.

# Objective and rules of the puzzle
# The objective is to move n number of disks from one tower to another following a set of rules.
# These rules are as follows:
# - Only one disk can be moved at a time
# - Only the upper disk of any of the towers can be moved
# - Larger disks cannot be placed over smaller disks

# In the optimal scenario of solving the puzzle, the total moves will be 2^n – 1 where n is the number of disks that need to be moved.


# Understanding codeblocks
# i begin with three towers or poles, source destination and helper.
# In the first section of code, i will cover the base condition of recursion.
# Base conditions serve primarily to complete the execution and ensure the recursion does not run into an infinite loop.
# The second section of code deals with the actual call to the recursion function within itself.
# The third section consists of the driver code for the initial call, consisting of the actual tower names that i pass as arguments to the function, along with the number of disks.
# Driver code is a generic term used to denote the section of code that gives the actual call to the function or class.

# Recursive function for Tower of Hanoi
def hanoi(disks, source, helper, destination):
    # Base Condition
    if disks == 1:
        # If there is only one disk, move it directly from the source tower to the destination tower
        print_tower_state(disks, source, destination)
        print('Move disk {} from tower {} to tower {}.'.format(disks, source, destination))
        return

    # Recursive calls in which function calls itself
    # Move n-1 disks from the source tower to the helper tower
    hanoi(disks - 1, source, destination, helper)
    # Move the largest disk from the source tower to the destination tower
    print_tower_state(disks, source, destination)
    print('Move disk {} from tower {} to tower {}.'.format(disks, source, destination))
    # Move the n-1 disks from the helper tower to the destination tower
    hanoi(disks - 1, helper, source, destination)

# Function to print the state of towers
def print_tower_state(moved_disk, source, destination):
    # Print the state of the towers after moving a disk
    print('After moving disk {} from {} to {}:'.format(moved_disk, source, destination))
    print("Tower A:", [" " * (disks - i) + "■" * (2 * i + 1) for i in range(disks, 0, -1)])
    print("Tower B:", [" " * disks for _ in range(disks)])
    print("Tower C:", [" " * disks for _ in range(disks)])
    print()  # Add an empty line for better visualization

# Driver code
disks = int(input('Number of disks to be displaced: '))

'''
Tower names passed as arguments:
Source: A
Helper: B
Destination: C
'''

# Initial state of the towers
# Tower A: [3, 2, 1], Tower B: [], Tower C: []
print("Initial state:")
print("Tower A:", [" " * (disks - i) + "■" * (2 * i + 1) for i in range(disks, 0, -1)])
print("Tower B:", [" " * disks for _ in range(disks)])
print("Tower C:", [" " * disks for _ in range(disks)])
print()  # Add an empty line for better visualization

# Actual function call
# Move all the disks from the source tower (A) to the destination tower (C) using the helper tower (B)
hanoi(disks, 'A', 'B', 'C')

