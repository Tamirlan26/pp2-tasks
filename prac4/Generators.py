#1
def s(n):
    for i in range(n + 1):
        yield i ** 2
n = 5
for sq in s(n):
    print(sq)
#2
def a(n):
    for i in range(n + 1):
        if i % 2 == 0:
            yield i
n = int(input())
print(','.join(str(x) for x in a(n)))
#3
def d(n):
    for i in range(n + 1):
        if i%3==0 and i%4==0:
            yield i
n = 50
for c in d(n):
    print(c, end=' ')
#4
def squares(a,b):
    for i in range(a, b+1):
        yield i**2
for val in squares(3, 7):
    print(val)