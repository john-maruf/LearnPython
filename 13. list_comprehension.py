a = [1, 10, 23, 24, 25, 26, 27, 28, 29, 30]

result = []

# print(10 / 3)
# print(10 // 3)
# print(10 % 3)

# for i in a:
#     if i % 2 == 0:
#         result.append(i)
# print(result)

# list comprehension
# result2 = [i for i in a if i % 2 == 0]
# print(result2)


# example of list comprehension with if else

b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result3 = [i**2 if i % 2 == 0 else i for i in b]
print(result3)
