#관계성이 있는 그룹의 저장 리스트 
#무작위로 밥값낼 사람 고르기 
import random

name = input("give me everybody'name seperated by a coma.: \n")
name_list = name.split(", ")
person_num = len(name_list) # input에서 받아온 사람 수 확인 
random_num = random.randint(1, person_num) #최대 수 정하는 변수 선언 

print(f"please pay Mr. or Ms.{name_list[random_num-1]}") #랜덤값 받아서 index로 활용

