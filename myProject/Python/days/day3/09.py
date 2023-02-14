# Welcome to Treasure Island your mission is to find the treasure
# you're at a cross road, where do you want to go? Type left or right ->right -> gameOver
# Swim or Wait -> Swim -> gameOver 
# Which Door ->red gameover
#Yellow you win / blue -> gameover 

print("Welcome to Treasure Island your mission is to find the treasure")
cross_road = input("left or right? : ")
cross_road = cross_road.lower()

if cross_road == "right":
    print("game over")
elif cross_road == "left":
    swim = input("swim or not? : ")
    swim = swim.lower()
    if swim == "swim":
        print("game over")
    elif swim == "not":
        door = input("choose door color blue, yellow, red : ")
        door = swim.lower()
        if door == "blue":
            print("game over")
        elif door == "yellow":
            print("you win")
        else:
            print("game over")
    
