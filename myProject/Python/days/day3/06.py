print("Welcome to the rollerCoaster")
height = int(input("what is your height is Cm?"))
age = int(input("what is your age?"))
photo = int(input("you want to photo? if you want to photo please input 1 want to not please input 2"))

photo_decision = False

if photo == 1:
    photo_decision = True
        
elif photo == 2:
    photo_decision = False
        
else:
    print("please input Collet Number")
        
    


if height > 120:
    print("you can ride the rollerCoaster")
    if age > 18:
        if photo:
            print(f"photo fee is ${12 +3}")
        else: 
            print(f"Total fee is ${12}")
    elif age > 12 or age < 18:
        if photo:
            print(f"photo fee is ${7+3}")
        else: 
            print(f"Total fee is ${7}")
    else:
        if photo:
            print(f"photo fee is ${5+3}")
        else: 
            print(f"Total fee is ${5}")
else:
    print("please next time come back to here when you taller 120Cm")
