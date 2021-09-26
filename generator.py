def gen(n):
    """Generator"""
    for i in range(n):
        yield i**2


g = gen(10)

for num in g:
    print(num)
