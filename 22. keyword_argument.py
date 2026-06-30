def my_func(f_name, l_name, age):
    print(f"My name is {f_name} {l_name} and I am {age} years old.")


my_func(age=24, f_name="John", l_name="Maruf")



# arbitary number of keyword arguments


def my_func(**kwargs):
    print(kwargs)
    print(
        f"My name is {kwargs['f_name']} {kwargs['l_name']}. I am {kwargs['age']} years old."
    )


my_func(age=24, f_name="John", l_name="Maruf")
