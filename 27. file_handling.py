import os
import pathlib

if os.path.exists("D:\\Python\\Module 2\\name.txt"):
    print("File exists")
else:
    print("File does not exist")

file_path = pathlib.Path = pathlib.Path("D:\\Python\\Module 2\\name.txt")
if file_path.exists():
    print("File exists")
print(os.path.abspath("D:\\Python\\Module 2\\name.txt"))
print(os.path.getsize("D:\\Python\\Module 2\\name.txt"))

with open("D:\\Python\\Module 2\\name.txt", "r") as f:
    print(f.tell())
