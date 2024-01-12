# bill = 175.00
# tax = 15
# total_tax = bill * tax / 100
# print(total_tax)

# ! This is Important
# Function definition
def calculate_tax(bill_amount, tax_rate):
    """
    Calculate tax based on the bill amount and tax rate.

    Parameters:
        bill_amount (float): The total amount of the bill.
        tax_rate (float): The tax rate to be applied.

    Returns:
        float: The calculated tax amount.
    """
    return (bill_amount * tax_rate) / 100

# Example usage
bill1 = 175.00
tax_rate1 = 15
total_tax1 = calculate_tax(bill1, tax_rate1)
print(f"For a bill of ${bill1} with a {tax_rate1}% tax rate, the total tax is: ${total_tax1:.2f}")

bill2 = 164.33
tax_rate2 = 15
total_tax2 = calculate_tax(bill2, tax_rate2)
print(f"For a bill of ${bill2} with a {tax_rate2}% tax rate, the total tax is: ${total_tax2:.2f}")
