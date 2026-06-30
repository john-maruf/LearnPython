import functools

# anonymous function - unnamed
# print kora jay
# she only return kore


def square(x):
    return x * x


print(square(5))


# lambda arguments

square = lambda x: x * x
print(square(4))

add = lambda a, b: a + b
print(add(1, 2))

students = [("John", 60), ("Maruf", 70)]
sorted_student = sorted(students, key=lambda x: x[1])
print(sorted_student)


# map(), filter(), reduce()
nums = [1, 2, 3, 4]
sq_nums = list(map(lambda x: x * x, nums))
print(sq_nums)

# filter

even = list(filter(lambda x: x % 2 == 0, nums))
print(even)


# reduce
sum = functools.reduce(lambda x, y: x + y, nums)
print(sum)
