password = input()
if (len(password) < 16):
  print("low")
else:
  print("good")
if password.isalpha() == True or password.isdigit() == True:
  print("loww")
else:
  print("goodd")