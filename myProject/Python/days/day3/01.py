#120cm를 넘어야 함 
print("Welcome to the rollerCoaster")
height = int(input("what is your height is Cm?"))

if height >= 120:
    print("you can ride RollerCoaster!")
elif height > 100 and height < 120:
    print("the next time")
else:
    print("good boy kid you have to grow taller before you can ride")