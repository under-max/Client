print("Welcome to the Love Calculator")
name1 = input("what is your name \n")
name2 = input("what is their name \n")

#lower function .lower() 소문자로 바꿔줌 
#count() 문자열에 몇번 나오는지 
#Angela.lower() -> 소문자로 변경해줌  
#Angela.count("a") -> 문자열에서 대상찾음 
# lover score 10 ~ 90 your -> your score is x, you go together like coke and mentos
# 40~50 your score is y, you are alright together
# others your score is z 


lower_name1 = name1.lower()
lower_name2 = name2.lower()

t_num1 = lower_name1.count("t")
r_num1 = lower_name1.count("r")
u_num1 = lower_name1.count("u")
e_num1 = lower_name1.count("e")

t_num2 = lower_name2.count("t")
r_num2 = lower_name2.count("r")
u_num2 = lower_name2.count("u")
e_num2 = lower_name2.count("e")

true_num1 = t_num1 + r_num1 + u_num1 + e_num1 # 10의 단위 
true_num2 = t_num2 + r_num2 + u_num2 + e_num2 # 10의 단위 

l_num1 = lower_name1.count("l")
o_num1 = lower_name1.count("o")
v_num1 = lower_name1.count("v")
e_num1 = lower_name1.count("e")

l_num2 = lower_name2.count("l")
o_num2 = lower_name2.count("o")
v_num2 = lower_name2.count("v")
e_num2 = lower_name2.count("e")
love_num1 = l_num1 + o_num1 + v_num1 + e_num1
love_num2 = l_num2 + o_num2 + v_num2 + e_num2

result = (true_num1 + true_num2) * 10 + love_num1 + love_num2

if result >= 10 and result <= 90:
    print(f"your score is {result}, you go together like coke and mentos")
elif result >= 40 and result <= 50:
    print(f"your score is {result}, you are alright together")
else:
    print(f"you score is {result}")

