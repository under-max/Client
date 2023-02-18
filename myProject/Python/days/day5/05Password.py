# 차례대로 비밀번호 생성 문자4 기호2 숫자 2 
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 
'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
'I', 'J', 'K' 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')']

print("Welcome to the pyPassword Generator")
nr_letters = int(input("How many letters would you like in your Password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
# for letter in letters:
#     print(letter)
#결국 리스트니까[]로 접근 []들어갈 숫자를 random 변수로 받아서 접근하면 될듯 
#letters = 몇개의 알파벳을 사용할껀지  
#symbols 몇개의 특수문자 사용할껀지 
#numbers 몇개의 숫자를 쓸껀지 
# user_letters = ""
# user_symbols = ""
# user_numbers = ""
# for ran in range(0, nr_letters):
#     user_letters += letters[random.randint(0, len(letters))]

# for ran in range(0, nr_symbols):
#     user_symbols += symbols[random.randint(0, len(symbols))]

# for ran in range(0, nr_numbers):
#     user_numbers += numbers[random.randint(0, len(numbers))]

# result = user_letters + user_symbols + user_numbers
# print(result)

# 어려운 level 문자 기호 숫자 취하는 대신 무작위 배치 쉬운 버전은 위에 완성 
# 전체를for로 감싸고 각 분기를 if 로 만들어서 전체 num 을 -- 시키고if 에서는 &&조건 false 하나로 두면
#작동 못하게 가능 할듯 
total_num = nr_letters + nr_symbols + nr_numbers
print(total_num)
result1 = ""
ran = random.randint(0, total_num)

for ran in range(0, total_num + 1):
    random_integer = random.randint(0,2)
    
    if (random_integer == 0) and (nr_letters != 0):
        result1 += letters[random.randint(0, len(letters))]
        nr_letters = nr_letters -1
       
        
    if (random_integer == 1) and (nr_symbols != 0):
        result1 += symbols[random.randint(0, len(symbols))]
        nr_symbols = nr_symbols - 1
        

    if (random_integer == 2) and (nr_numbers != 0):
        result1 += numbers[random.randint(0, len(numbers))]
        nr_numbers = nr_numbers -1
                
print(result1)
