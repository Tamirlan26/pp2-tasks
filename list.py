#1
thislist = ["apple", "banana", "cherry"]
print(thislist[1])
#2
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])
#3
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)
#4
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)
#5
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)
#6
thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print(thislist)
#7
thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)
#8
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)
#9
def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)
#10
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)
#11
