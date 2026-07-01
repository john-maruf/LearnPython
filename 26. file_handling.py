# with open("D:\\Python\\Module 2\\name.txt", "w") as f:
#     f.write("Hello, World!\n")
#     f.write("This is a test file.\n")

with open("D:\\Python\\Module 2\\name.txt", "a") as f:
    f.write("\nHello, World!\n")
    f.write("This is a test file.")

lines = ["\n i love python", "\n i love programming", "\n i love coding"]

with open("D:\\Python\\Module 2\\name.txt", "a") as f:
    f.writelines(lines)
