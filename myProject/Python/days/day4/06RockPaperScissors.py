#가위바위보 0 = 바위 1 = 보  2= 가위
import random
user_num = input("what do you choose? type 0 for Rock, 1 for paper, 2 for Scissors : ")
com_num = random.randint(1,3) # 랜덤값 
item = ["✊","🖐️","🤏"]
com_result = ""
user_result = ""
if com_num == 1:
    com_result = "✊"
elif com_num == 2:
    com_result = "🖐️"
else: 
    com_result = "🤏"

if user_num == 1:
    user_result = "✊"
elif user_num == 2:
    user_result = "🖐️"
else: 
    user_result = "🤏"


if user_result == com_result:
    print("draw")
elif (user_num != com_num): 

#이기는 경우             #지는 경우     
#가위 보  2가 1보나 큼    가위 바위
#바위 가위                바위 보
#보 바위                  보 가위 

#
