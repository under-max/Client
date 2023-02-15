import random


random_int = random.randint(1, 10)
print(random_int)

random_float = random.random() #0.0~ 0.99까지 반환
random_float *= 100
print(int(random_float))