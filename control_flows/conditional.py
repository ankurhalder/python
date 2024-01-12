bill_total = 220

discount1 = 10
discount2 = 20

if bill_total >= 100 and bill_total < 200:
    print("Yout Bill is greater than 100")
    bill_total = bill_total - discount1
elif bill_total >= 200:
    print("Your Bill is greater than 200")
    bill_total = bill_total - discount2
else:
    print("Your Bill is less than 100")
    
    
print("Your Bill Total is: ", bill_total)