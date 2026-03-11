def our_range(start, stop, step=1):
    while((step > 0 and start < stop) or (step < 0 and start > stop)):
        yield start
        start += step

start = int(input())
stop = int(input())
step = int(input())

for num in our_range(start, stop, step):
    print(num)