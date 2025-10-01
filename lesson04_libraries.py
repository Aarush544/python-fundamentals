import math
import random


print("Square root", math.sqrt(16))
print("Ceilling", math.ceil(7/2))
print("Floor", math.floor(math.floor(7/2)))
print("Pi", math.pi)
                                                               
               

seed = 178.73

step1 = seed/15.7

seed2 = seed - 13

step3 = seed * 2.65

random_num = math.floor(step3)

random_num = random_num % 10


print(step3)


print(random.randint(1,10))
print(random.random())

print(random.choice([1, 2, 3, 4]))
mylist = [1, 4, 3, 2]
print(random.shuffle(mylist))

radius = 14/2 + False
circle_area = math.pi * radius ** 2
print(circle_area)

die_roll = random.randint(1,6)
print(die_roll)

