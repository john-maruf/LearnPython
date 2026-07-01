# a region where a variable accessible

x = 10  # global variable

print(x)


def func():
    y = 19  # local variable
    x = 200
    print("x", x)
    print("y", y)


func()
print(x)

# LEGB
# l - local
# E - enclosing
# G - global
# B - built-in Scope (print, sum, max, input)

n = "global"  # global variable


def outer():
    n = "enclosing"  # enclosing variable

    def inner():
        # global n  # just global variable ke update kore
        nonlocal n  # enclosing variable ke update kore
        n = "local"  # local variable
        print(n)

    inner()
    print(n)


outer()
print(n)
