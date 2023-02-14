#
year = int(input("which year do you want to check? : "))

#2020 / 4 는 나머지 없으면 윤년
#예외로 100으로 나눠지면 윤년 아님
#하지만 해가 400으로 나눠지면 여전히 윤년

if (year % 100 == 0) or (year % 400 == 0) or (year % 4 == 0):
    print("Leap Year!")
else:
    print("it is no Leap Year!")


