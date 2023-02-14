#BMI 계산기
height = input("Enter your height in m : ")
weight = input("ENter your weight in Kg : ")

result = int(weight) / float(height) ** 2
bmi = int(result)
print(bmi) 