nums = [5, 10, 15, 20]
a=iter(nums)
print(next(a))
print(next(a))
#2
text = "Python"
b=iter(text)
print(next(b))
print(next(b))
print(next(b))
#3
a=iter(range(1,6))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
#4
nums = [1, 2, 3]
a=iter(nums)
print(next(a)) 
for i in a:
    print(next(i))
#5
d = {"a": 1, "b": 2, "c": 3}
it = iter(d)

k = next(it)
print(k, d[k])   # первый ключ + значение

for key in it:
    print(key, d[key])
#6
a=[1,2,3]
b=iter(a)
while True:
    print(next(b))
#7
a=[100,200,300,400]
b=iter(a)
print(next(b))
for i in b:
    print(i)
    