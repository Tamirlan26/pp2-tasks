def a(n):
    for i in range(0,n+1):
        if i%3==0 and i%4==0:
            yield i
n=int(input())
b=a(n)
t=True
for i in b:
    print(i,end=" ")