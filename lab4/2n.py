#1
def even_numbers(n):
    for i in range(n + 1):
        if i % 2 == 0:
            yield i

n = int(input())

first = True
for x in even_numbers(n):
    if not first:
        print(",", end="")
    print(x, end="")
    first = False

#2
def even_numbers(n):
    for i in range(0, n + 1, 2):  
        yield i

n = int(input())

print(",".join(map(str, even_numbers(n))))