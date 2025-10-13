print("rubles")
sum = int(input())
print (sum // 100, '100r')
sum %= 100
print (sum // 50, '50r')
sum %= 50
print (sum // 20, '20r')
sum %= 20
print (sum // 10, '10r')
sum %= 10
print (sum // 5, '5r')
sum %= 5
print (sum // 2, '2r')
sum %= 2
print (sum // 1, '1r')
sum %= 1