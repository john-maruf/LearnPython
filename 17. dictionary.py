# key value pair
# indexing er shujog nai
# key gula must immutable

a = {1: "one", 2: "two", 3: "three", 4: {1, 2, 3}}
print(type(a))
for i in a:
    print(i)  # key gula print hobe

print(".........")
for i in a.values():
    print(i)  # value gula print hobe

print(a.keys(), a.values())

print(".........")
for k, v in a.items():
    print(f"key name: {k} , value: {v}")

print(".........")
a = [1, 2, 3, 4]
b = ["mango", "banana", "apple", "orange"]
c = dict(zip(a, b))

print(dict(zip(a, b)))  # zip object
print(c[1])
