import random
a=1
b=100
c = (random.randint(a, b))
d=int(input("введите число от 1 до 100: "))
while True:
    if c > d:
     print("больше")
     d=int(input("введите другое число от 1 до 100: "))
    if c < d:
     print("меньше")
     d=int(input("введите другое число от 1 до 100: "))
    if c == d:
     print("победа")
     break