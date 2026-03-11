def a(c,b):
    for i in range(c,b+1):
        yield i*i
c,b=map(int,input().split())
b=a(c,b)
for i in b:
    print(i)