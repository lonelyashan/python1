ss = [50,25,51,11,32,21,34,23]
ns = [i for i in ss if i % 2 == 1]
ps = [i for i in ss if i % 2 == 0]
nn=0
pp=0
for i in ns:
    nn += i
for i in ps:
    pp += i
print(abs(nn-pp))