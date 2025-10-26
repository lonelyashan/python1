c = int(input())
c1 = 0.89
s = int(input())
s1 = 0.69
i = int(input())
i1 = 0.79
c2 = 0
s2 = 0
i2 = 0
if c > 60:
    c2 = (c - 60) * c1
    print("лишний расход минут:", c2)
if s > 30:
    s2 = (s - 30) * s1
    print("лишний расход sms:", s2)
if i > 1024:
    i2 = (i - 1024) * i1
    print("лишний расход mb:", i2)
ssu = 24.99 + c2 + s2 + i2
ssu += ssu*0.02
print(round(ssu, 2))