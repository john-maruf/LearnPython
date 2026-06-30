# no input , no return


def my_function():  # function definition
    a = 10
    b = 12
    print(a + b)


my_function()  # function call


# input , no return


def add_two_numbers(a, b):
    print(a + b)


add_two_numbers(5, 7)
add_two_numbers(10, 15)

# input , return


def multiply_two_numbers(a, b):
    return a * b


result = multiply_two_numbers(13, 2)
print(result)


# no input , return
def hello():
    return "Hello"


greeting = hello()
print(greeting)
