#1
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]

thisset.update(mylist)

print(thisset)
#2
thisset = {"apple", "banana", "cherry"}

thisset.add("orange")

print(thisset)
#3
thisset = {"apple", "banana", "cherry"}

thisset.remove("banana")

print(thisset)
#4
thisset = {"apple", "banana", "cherry"}

thisset.discard("banana")

print(thisset)
#5
thisset = {"apple", "banana", "cherry"}

x = thisset.pop()

print(x)

print(thisset)
#6
thisset = {"apple", "banana", "cherry"}

del thisset

print(thisset)
#7
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)
#8
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1 | set2
print(set3)
#9
x = frozenset({"apple", "banana", "cherry"})
print(x)
print(type(x))
