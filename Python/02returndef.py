def tax_calc(money):
    return money * 0.35

to_pay = tax_calc(200000)

def pay_tax(tax):
    print("Tankyou for your Paying", tax)

pay_tax(tax_calc(200000000))#함수안에 함수 소환가능

#문자열안에 변수 넣는방법
my_name = "nick"
my_age = 12
my_eye = "brown"

print(f"Hello i'm {my_name}, i have {my_age}, years in the earth") #f앞에 넣고 변수에서만 {}

# 
def make_juice(fruit):
    return f"{fruit}+a"

def add_ice(juice):
    return f"{juice}+b"

def add_sugar(iced_juice):
    return f"{iced_juice}+c"

juiice = make_juice("apple") #apple 라고 가지고이는 상태 
cold_juice = add_ice(juiice) #
perferct_juice = add_sugar(cold_juice)

print(perferct_juice)
