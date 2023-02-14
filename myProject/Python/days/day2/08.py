print("Welcome to the tip Calculator")
price = float(input("what was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
person = int(input("How many people to split the bill? "))
tip = tip / 100
total_price = price + tip
each_price = total_price / person
print(f"Each person should pay : {each_price}") 

