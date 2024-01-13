# Initial bill total
bill_total = 220

# Discounts
discount1 = 10
discount2 = 20

# Check bill amount and apply discounts
if 100 <= bill_total < 200:
    # If the bill is between 100 and 200, apply discount1
    print("Your bill is between 100 and 200.")
    bill_total -= discount1
elif bill_total >= 200:
    # If the bill is greater than or equal to 200, apply discount2
    print("Your bill is greater than or equal to 200.")
    bill_total -= discount2
else:
    # If the bill is less than 100, no discount is applied
    print("Your bill is less than 100.")

# Display the final bill total
print("Your Bill Total is:", bill_total)
