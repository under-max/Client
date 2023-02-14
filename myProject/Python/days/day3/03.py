#120cm를 넘어야 함 
print("Welcome to the rollerCoaster")
height = int(input("what is your height is Cm?"))
age = int(input("what is your age?"))

if height >= 120:
    print("you can ride RollerCoaster!")
    if age >=18:
        print("18box")
    else:
        print("10box")
else:
    print("good boy kid you have to grow taller before you can ride")