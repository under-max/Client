print("hello!")

a = 2
b = 3
c = a + b
print(c)

d = "Hello"
print(d)

e = False
f = True

dead = True
Alive = False 

print("Hello", a ,"your also", d)

print(12)
print("Hello")
print(True, "HEy")

def say_Hello():
    print("Who are you")

def say_Hi(name):
    print(name, "Hi")

say_Hi("Nick")

def add(num1, num2):
    return num1 + num2

x = add(2,3)
print(x)
print(add(1,2))

def HiHi(name, age):
    print(name, "님", age, "이시네요")
    
HiHi("Nick", 25)

def tax_calculation(money, rate):
    print(money * rate)

tax_calculation(15000000000, 0.25)

def say_hi(name="Anonymous"): #정의되지 않은 변수값에 대해서 =으로 constructure 처럼 사용할 수 있음 
    print("say", name)

say_hi("Nick")
say_hi()


def plus(a=False, b=False):
    print(a+b)

def dis(a=False, b=False):
    print(a-b)

def mul(a=False, b=False):
    print(a*b)

def div(a=False, b=False):
    print(a/b)

def dob_mul(a=False, b=False):
    print(a ** b)

print(2**4)
plus()
plus(2,3)

dis()
dis(4,2)

mul()
mul(4,2)

div()
div(4,2)

dob_mul()
dob_mul(3,2)
