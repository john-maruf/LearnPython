def addition(*args):
    print(args)
    return sum(args)


r = addition(5, 10, 15, 20, 25)
print(r)
