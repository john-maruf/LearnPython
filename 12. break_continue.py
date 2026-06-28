a = [1, 2, 3, 4, 5, "a", 6, 7, 8, 9, 10]

for i in a:
    if type(i) == type("a"):
        break
    else:
        print(i)
print("loop breaked successfully")

for i in a:
    if type(i) == type("a"):
        continue
    else:
        print(i)
print("loop continued successfully")
