#max()함수 리스트 안에 가장 큰 값을 찾음 
#min()함수 리스트 안에 가장 작은 값을 찾음 
#for문만 사용해서 최대값 찾기 

student_score = input("input a list of student score").split(", ")
for n in range(0, len(student_score)):
    student_score[n] = int(student_score[n])
print(student_score)

max = 0
for check in student_score:
    print(check)
    if max < check:
        max = check

print(max)