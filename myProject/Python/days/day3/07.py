print("Welcome to Python Pizza Deliveries")
size = input("what size pizza do you want : ") #"L" "M" "S"
add_peperoni = input("Do you want peperoni? : ") #"Y" "N"
extra_cheese = input("Do you want extra cheese? : ") #"Y" "N"

small_pizza = 15
medium_pizza = 20
large_pizza = 25

if size == "L":
    if add_peperoni == "Y":
        large_pizza += 3
        if extra_cheese == "Y":
            large_pizza += 1
            print(f"your final bill is {large_pizza }")
        elif extra_cheese == "N":
            print(f"your final bill is {large_pizza}")
    else:
        if extra_cheese == "Y":
            large_pizza +=1
            print(f"your final bill is {large_pizza}")
        elif extra_cheese == "N":
            print(f"your final bill is {large_pizza}")

elif size == "M":
    if add_peperoni == "Y":
        large_pizza += 3
        if extra_cheese == "Y":
            large_pizza += 1
            print(f"your final bill is {large_pizza }")
        elif extra_cheese == "N":
            print(f"your final bill is {large_pizza}")
    else:
        if extra_cheese == "Y":
            large_pizza +=1
            print(f"your final bill is {large_pizza}")
        elif extra_cheese == "N":
            print(f"your final bill is {large_pizza}")
else:
    if add_peperoni == "Y":
        large_pizza += 2
        if extra_cheese == "Y":
            large_pizza += 1
            print(f"your final bill is {large_pizza }")
        elif extra_cheese == "N":
            print(f"your final bill is {large_pizza}")
    else:
        if extra_cheese == "Y":
            large_pizza +=1
            print(f"your final bill is {large_pizza}")
        elif extra_cheese == "N":
            print(f"your final bill is {large_pizza}")


#small pizza = $15
#medium pizza = $20
#large pizza = $25

#peperoni for small pizza = +$2
#peperoni for Medium or Large Pizza = +$3
#extra cheese for any size Pizza: $+1


#example input 
#size = "L"
#add_peperoni = "Y"
#extra_cheese = "N" 

#your final bill is : 