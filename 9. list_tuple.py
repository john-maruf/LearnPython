a = [1, 2, 3, "john", " maruf", 4.5, 5.6, 6.7]
# a[0] = 100
# print(a)
# print(a[-1])
# print(len(a))

# s = "hello"
# print(list(s))


a.append([1, 2, 3])
print(a)
print(a.index("john"))
a.reverse()
print(a)

# tuple
t = (1, 2, 3)
t_r = tuple(reversed(t))
print(t)
print(t_r)
