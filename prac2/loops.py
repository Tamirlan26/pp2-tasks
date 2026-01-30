#1
i = 1
while i < 6:
  print(i)
  i += 1
#2
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1
#3
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)
#4
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break
#5
for x in range(6):
  if x == 3: break
  print(x)
else:
  print("Finally finished!")
#6
for x in [0, 1, 2]:
  pass