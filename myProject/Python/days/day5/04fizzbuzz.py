#시계방향으롷 움직임 
#3으로 완전히 나눌수 있는 어떤 숫자면 fizz
#5로 완전히 나눌수 있는 숫자면 buzz
#3과 5로 완전히 나눌수 있는 경우fizz buzz

for number in range(1, 101):
    
    if(number % 3 == 0) and (number % 5 == 0):
        print("Fizz Buzz")
    elif(number % 3 == 0):
        print("Fizz")
    elif(number % 5 ==  0):
        print("Buzz")
    