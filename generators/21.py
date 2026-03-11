def nums():
    start = 1
    while(start < 10):
        yield start
        start += 1

nums_gen = nums()

print(nums_gen)

print(next(nums_gen))
print(next(nums_gen))
print(next(nums_gen))