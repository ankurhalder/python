# bill = 175.00
# tax = 15
# total_tax = bill * tax / 100
# print(total_tax)


def calculate_tax(bill, tax_rate):
    return ((bill * tax_rate) / 100)

print("Total Tax", calculate_tax(175.00, 15))

print("Total Tax", calculate_tax(164.33, 15))