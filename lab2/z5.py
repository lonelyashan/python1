t1 = ("few", "found", "fear")
mx = 0
e1 = 0
for i in t1:
    if len(i) > mx:
        mx = len(i)
        e1 = i
print(e1)