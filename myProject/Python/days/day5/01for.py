#평균신장 구하기
#평균 입력을 위한 키 180, 124, 165, 173, 189, 169, 146
#sum 제공 함수 쓰지 말것 
student_heights = input("Input a list of students").split(", ")
for n in range (0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
print(student_heights)
sum = 0

count = 0
for a in student_heights:
    count = count + 1 #인원수 확인 

for b in student_heights:
    sum += b #신장의 총합
print(int(sum / count))
