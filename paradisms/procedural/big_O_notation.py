# Intro to Big-O notation
"""
Big O notation is a fundamental concept in computer science and programming that helps you analyze and describe the efficiency of algorithms. It provides a standardized way of expressing how the runtime or resource usage of an algorithm grows as the size of the input data increases.
"""

# What is Big O Notation?
"""
Big O notation is a mathematical notation that describes the upper bound or worst-case scenario for the time complexity of an algorithm. It helps us answer questions like:

- How does the runtime of an algorithm change as the input data gets larger?
- How does an algorithm scale with increased input size?

Big O notation is written as "O(f(n))," where "f(n)" is a function that represents the relationship between the input size (usually denoted as "n") and the algorithm's runtime or resource usage.
"""

# Common Examples of Big O Notation

# O(1) - Constant Time
"""
No matter how large the array is, accessing an element by its index takes the same amount of time. The runtime is constant, and we denote it as O(1).
"""
def constant_time_example(arr):
    return arr[0]

# O(n) - Linear Time
"""
As the size of the list (arr) increases, the number of iterations the loop performs also increases linearly. Therefore, this algorithm has a time complexity of O(n).
"""
def linear_time_example(arr, target):
    for item in arr:
        if item == target:
            return True
    return False

# O(n^2) - Quadratic Time
"""
Bubble sort has a time complexity of O(n^2). As the size of the input list (arr) increases, the number of comparisons and swaps grows quadratically.
"""
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# O(log n) - Logarithmic Time
"""
Binary search drastically reduces the search time as the size of the sorted list (arr) grows. It has a time complexity of O(log n).
"""
def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return True
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return False

# O(n log n) - Linearithmic Time
"""
Merge sort is an example of linearithmic time complexity. It's faster than quadratic but slower than linear.
"""
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

# O(2^n) - Exponential Time
"""
An example of exponential time complexity is the recursive calculation of Fibonacci numbers.
"""
def fibonacci_recursive(n):
    if n <= 1:
        return n
    return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

# O(n!) - Factorial Time
"""
An example of factorial time complexity is the permutation of elements in a list.
"""
import itertools

def permutations(arr):
    return list(itertools.permutations(arr))

# O(n^k) - Polynomial Time
"""
Polynomial time complexity, where 'k' is a constant, is often seen in algorithms with nested loops but not as severe as exponential time.
"""
def polynomial_time(arr):
    n = len(arr)
    for i in range(n):
        for j in range(i, n):
            # Placeholder operation
            pass
# O(sqrt(n)) - Square Root Time
"""
Square root time complexity is less common but can appear in certain algorithms.
"""
import math

def square_root_time(arr):
    n = len(arr)
    for i in range(0, int(math.sqrt(n))):
        # Placeholder operation
        pass

# O(log log n) - Double Logarithmic Time
"""
Double logarithmic time complexity is very rare and often seen in specific scenarios.
"""
def double_logarithmic_time(arr):
    n = len(arr)
    i = 1
    while i < n:
        # Some operation on arr[i]
        i = i * i

# Additional Big O Theories

# Space Complexity
"""
Big O notation can also be used to analyze space complexity, representing how the space requirements of an algorithm grow as the input size increases.
"""
def space_complexity_example(n):
    arr = [0] * n
    return arr

# Amortized Analysis
"""
Amortized analysis considers the average time taken per operation over a sequence of operations. It helps in situations where some operations are more expensive but are balanced by cheaper operations.
"""
def amortized_analysis_example(n):
    operations = []
    for i in range(n):
        # Some operation
        operations.append(i)
    return operations

# Optimal Algorithms
"""
Choosing the right algorithm can significantly impact performance. For example, using a set for membership tests can have better average-case time complexity than a list.
"""
def optimal_algorithm_example(lst, target):
    return target in set(lst)

# Dynamic Programming
"""
Dynamic programming is a technique where a complex problem is broken down into simpler overlapping subproblems, and the solutions to these subproblems are memoized to avoid redundant calculations.
"""
def fibonacci_dynamic_programming(n, memo={}):
    if n <= 1:
        return n
    if n not in memo:
        memo[n] = fibonacci_dynamic_programming(n-1, memo) + fibonacci_dynamic_programming(n-2, memo)
    return memo[n]

# Greedy Algorithms
"""
Greedy algorithms make locally optimal choices at each stage with the hope of finding a global optimum. They are often used in optimization problems.
"""
def coin_change_greedy(coins, amount):
    coins.sort(reverse=True)
    count = 0
    for coin in coins:
        count += amount // coin
        amount %= coin
    return count

# Divide and Conquer
"""
Divide and conquer is a strategy where a problem is broken down into smaller subproblems, solved independently, and then combined to solve the original problem.
"""
def binary_search_divide_and_conquer(arr, target):
    if not arr:
        return False
    mid = len(arr) // 2
    if arr[mid] == target:
        return True
    elif arr[mid] < target:
        return binary_search_divide_and_conquer(arr[mid+1:], target)
    else:
        return binary_search_divide_and_conquer(arr[:mid], target)

# Randomized Algorithms
"""
Randomized algorithms use random inputs to make decisions, and their performance is evaluated based on the expected behavior over all possible random inputs.
"""
import random

def randomize_array(arr):
    random.shuffle(arr)
    return arr

# In-Place Algorithms
"""
In-place algorithms modify the input data structure without requiring extra space proportional to the input size.
"""
def reverse_in_place(arr):
    left, right = 0, len(arr) - 1
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
    return arr

# Parallel Algorithms
"""
Parallel algorithms divide a problem into subproblems that can be solved independently, often leading to improved performance in parallel computing environments.
"""
from multiprocessing import Pool

def parallel_sum(arr):
    with Pool() as pool:
        return sum(pool.map(lambda x: x*x, arr))

# Quantum Algorithms
"""
Quantum algorithms leverage the principles of quantum mechanics, such as superposition and entanglement, to perform certain computations more efficiently than classical algorithms.
"""
# Example: Quantum Search Algorithm (Grover's Algorithm)

# Why Big O Notation Matters
"""
Big O notation is crucial for several reasons, including algorithm comparison, performance optimization, scalability, resource management, and coding interviews.
"""

# Analyzing Code with Big O Notation
"""
Steps to analyze code using Big O notation, including identifying the input size, loops, counting operations inside loops, combining complexity, choosing the dominant term, and simplifying the expression.
"""

# Optimizations and Best Practices
"""
Various optimization techniques and best practices, such as amortized analysis, space complexity analysis, optimal algorithm selection, dynamic programming, greedy algorithms, divide and conquer, randomized algorithms, in-place algorithms, parallel algorithms, and quantum algorithms.
"""

# In summary
"""
Big O notation is a fundamental concept in computer science that helps us analyze and compare algorithms' efficiency. By understanding its basics and applying it to code, you can make informed decisions about algorithm selection and optimization, ensuring your programs run efficiently, even as data sizes grow.
"""
