def a(b):
    for i in range(b, -1, -1):
        yield i

b = int(input())
c = a(b)

for i in c:
    print(i)