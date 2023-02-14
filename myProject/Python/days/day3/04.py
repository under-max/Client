height = float(input("Enter your height in m: "))
weight = float(input("Enter your weight in Kg: "))

result = round(weight / (height ** 2))
print(result)

if result < 18.5:
    print(f"your bmi is {result} underweight")
elif result >= 18.5 and result <= 25:
    print(f"your bmi is {result} normal weight")
elif result >= 25 and result <= 30:
    print(f"your bmi is {result} over weight")
elif result >= 30 and result >= 35:
    print("your bmi is {result} obese")
else:
    print("your bmi is {result} Clinically obese") 