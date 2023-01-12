def generator_funkc(num):
    for sk in range(num):
        yield sk

# for item in generator_funkc(20):
#     print(item)

g = generator_funkc(20)
next(g)
next(g)
print(next(g))