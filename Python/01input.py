from random import randint
a = int(input("input Number"))
b = int(input("input Number")) #String 으로 저장됨 #형변환 int(input("hi"))

#&& =and  || = or

print(type(a)) #String 인지 interger 인지 float 인지 확인

def add(num1,num2):
    return num1+num2

print(add(a,b))

#컴퓨터가 번호하나 선택 유저가 하나 선택 

user = int(input("choose your number"))
pc = randint(1,50) #import 시켜야함 from random import randint

if user == pc :
    print("your won")
elif user < pc : 
    print("Lower! Computer Choice", pc)
elif user > pc :
    print("Higher! Computer Choice", pc)

