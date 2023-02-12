#datastructure - 데이터 구조화 하고 싶을떄 
#tuple, list 

days = ["mon", "sat", "sun"] #list
print(days)
print(days[0])

name = "rick"
print(name.upper()) #.upper()는 함수 ()가 없으므로 붙여줘야함    
print(name.startswith("n")) #n으로 시작하는지 
print(name.replace("c", "C")) #교체
print(name.endswith("k")) #k로 끝나는지

days.reverse()
print(days)

days.append("WEd")
print(days)

days.__sizeof__()
print(days.__sizeof__())