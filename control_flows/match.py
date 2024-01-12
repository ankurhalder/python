http_status = 201

match http_status:
    case 200| 201:
        print("OK")
    case 400:
        print("Bad Request")
    case 404:
        print("Not Found")
    case 500:
        print("Internal Server Error")
    case _:
        print("Unknown Status Code")