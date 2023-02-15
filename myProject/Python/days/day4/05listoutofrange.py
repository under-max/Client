#index 의 범위를 벗어남 index out of range / off by one 이라고도 함 
#len 으로 확인시 1더 많기떄문에 유의할것
#리스트안에 리스트 중첩리스트 
#관련있는 리스트 끼리 새로운 리스트를 만들어서 합침
sun = "🌞"
row1 = ["🔒", "🔒", "🔒"]
row2 = ["🔒", "🔒", "🔒"]
row3 = ["🔒", "🔒", "🔒"]

map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("where do you want put the treasure? : ")
position_x = int(position[0]) - 1 # x 좌표 값
position_y = int(position[3]) - 1 # y 좌표 값 


map[position_y][position_x] = "🌞"


print(f"{row1}\n{row2}\n{row3}")
