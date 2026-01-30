#!
a = 33
b = 200
#if b > a:
#print("b is greater than a") erro
#2
a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
#3
age = 25

if age < 13:
  print("You are a child")
elif age < 20:
  print("You are a teenager")
elif age < 65:
  print("You are an adult")
elif age >= 65:
  print("You are a senior")
#4
a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")
#5
a = 5
b = 2
if a > b: print("a is greater than b")
#6
a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")
#7
x = 41

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")