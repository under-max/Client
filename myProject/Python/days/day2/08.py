print("Welcome to the tip Calculator")
total_bill = float(input("what was the total bill? $"))
percentage = float(input("What percentage tip would you like to give? 10, 12, or 15? "))
bill_with_tip = percentage / 100 * total_bill
print(bill_with_tip)
person = int(input("How many people to split the bill? "))
total = total_bill + bill_with_tip
total = total / person
total = round(total, 2)
print(f"Each person should pay : {total}") 