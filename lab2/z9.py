def cou (n):
    can = 0
    for i in range (1, n+1):
        if n % i == 0:
         can += 1
    return can
n = int(input())
ss = {}
for i in range (1, n+1):
    ss[i]=cou(i)
print(ss)