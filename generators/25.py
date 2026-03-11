def our_range(start, stop, step=1):
    while((step > 0 and start < stop) or (step < 0 and start > stop)):
        yield start
        start += step

for num in our_range(10, 1, -1):
    print(num)