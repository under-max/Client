#Key value 로 이루어짐 
player = {
    "name": "nico",
    "age" : 12,
    'alive': True,
    "fav_food": ["pizza", "burger"]
}

print(player.get("age")) #list 에서는 이렇게 할수 없지만 dictionary 에서는 키 - 쌍으로 이루어져 있어서 가능
print(player.get("fav_food")) #보통 데이터를 만들때 사용함 
#pop key 를 지움
player.pop("age") 
print(player)
player['xp'] = 15000 #dictionalry 에 추가
print(player)
player["fav_food"].append("noodle")
print(player)
print(player.get("fav_food"))