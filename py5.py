print("number")
ss = input()
number = int(ss)
summ = int(0)
if number % 7 == 0:
    print("magic number!")
else:
 for i in range(len(ss)):
    s=int(ss[i])
    summ = summ + s
 print(summ)