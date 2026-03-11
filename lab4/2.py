def test():
    print("A")
    yield 1
    print("B")
    yield 2

g = test()

print("First call:")
print(next(g))

print("Second call:")
print(next(g))