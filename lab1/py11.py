a = int(input("enter day number: "))
b = int(input("enter month number: "))
if a>=21 and a<=31 and b == 3 or a>=1 and a<=19 and b == 4:
    print("овен")
elif a>=20 and a<=30 and b == 4 or a>=1 and a<=20 and b == 5:
    print("телец")
elif a>=21 and a<=31 and b == 5 or a>=1 and a<=20 and b == 6:
    print("близнецы")
elif a>=21 and a<=30 and b == 6 or a>=1 and a<=22 and b == 7:
    print("рак")
elif a>=23 and a<=31 and b == 7 or a>=1 and a<=22 and b == 8:
    print("лев")
elif a>=23 and a<=31 and b == 8 or a>=1 and a<=22 and b ==9:
    print("дева")
elif a>=23 and a<=30 and b == 9 or a>=1 and a<=22 and b ==10:
    print("весы")
elif a>=23 and a<=31 and b == 10 or a>=1 and a<=21 and b ==11:
    print("скорпион")
elif a>=22 and a<=30 and b == 11 or a>=1 and a<=21 and b == 12:
    print("стрелец")
elif a>=22 and a<=31 and b == 12 or a>=1 and a<=19 and b == 1:
    print("козерог")
elif a>=20 and a<=31 and b == 1 or a>=1 and a<=18 and b == 2:
    print("водолей")
elif a>=19 and a<=29 and b == 2 or a>=1 and a<=20 and b == 3:
    print("рыбы")
else:
    print("invalid input")
