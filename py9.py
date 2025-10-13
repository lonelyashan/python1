address = input()
add = address.split('.')
if (len(add)!=4 or address.count('.')!=3 or not
all (list(map(lambda x: (0<=int(x)<=255), add)))):
    print("invalid format")
else:
    print("right format")



