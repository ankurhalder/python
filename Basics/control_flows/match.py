# HTTP status code
http_status = 201

# Using match statement
match http_status:
    case 200 | 201:
        print("OK")
    case 400:
        print("Bad Request")
    case 404:
        print("Not Found")
    case 500:
        print("Internal Server Error")
    case _:
        print("Unknown Status Code")

# Using patterns in match
value = [1, 2, 3]

match value:
    case [1, 2, 3]:
        print("Pattern matched: [1, 2, 3]")
    case [1, x, 3] if x > 0:
        print(f"Pattern matched: [1, {x}, 3] where x is positive")

# Matching with types
match value:
    case val if isinstance(val, int):
        print("The value is an integer")
    case val if isinstance(val, list):
        print("The value is a list")
    case _:
        print("Unknown type")

# Using match in functions
def process_status_code(status_code):
    match status_code:
        case 200 | 201:
            return "OK"
        case 400:
            return "Bad Request"
        case 404:
            return "Not Found"
        case 500:
            return "Internal Server Error"
        case _:
            return "Unknown Status Code"

# Call the function with a status code
result = process_status_code(404)
print("Result:", result)
