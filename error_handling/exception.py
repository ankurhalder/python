def divide_numbers(num1, num2):
    try:
        # Attempting to perform the division
        result = num1 / num2

        # Printing the result if successful
        print(f"Result of division: {result}")

    except ZeroDivisionError:
        # Handling division by zero error
        print("Error: Division by zero is not allowed")

    except TypeError as e:
        # Handling type error, for example, if trying to divide a string
        print(f"Error: {e}")

    except (ValueError, RuntimeError):
        # Handling multiple types of exceptions using a tuple
        print("Error: Value or Runtime error occurred")

    except FileNotFoundError:
        # Handling file not found error
        print("Error: File not found")

    except IndexError:
        # Handling index out of range error
        print("Error: Index out of range")

    except KeyError:
        # Handling key not found error
        print("Error: Key not found")

    except AttributeError:
        # Handling attribute error
        print("Error: Attribute not found")

    except NameError:
        # Handling name error (undefined variable)
        print("Error: Name not defined")

    except Exception as e:
        # Handling any other unexpected exceptions
        print(f"Unexpected Error: {e}")

    else:
        # Executed if no exception occurs
        print("Division successful")

    finally:
        # Always executed, used for cleanup or finalization
        print("Finally block: This code always runs")


# Example usage
try:
    # Asking the user for input
    num1 = float(input("Enter the numerator: "))
    num2 = float(input("Enter the denominator: "))

    # Calling the function with user inputs
    divide_numbers(num1, num2)

except ValueError:
    # Handling value error, for example, if the user enters a non-numeric input
    print("Error: Invalid input. Please enter numeric values.")
