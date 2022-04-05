# import random
#
# while True:
#     random_choice = random.choice([x for x in range(10)])
#     if(random_choice % 3 == 0):
#         break
#     print(random_choice)
#
# print(f'random choice: {random_choice}')
#
# def my_sum(a, b):
#     return a + b
#
# print(my_sum(1, 3))
#
# def my_func(list):
#     list.append(10)
#
# my_list = [2, 3, 4]
# my_func(my_list)
#
# print(my_list)
#
# def my_sum_again(*args):
#     acc = 0
#     for arg in args:
#         acc += arg
#     return acc
#
# my_sum_again(2, 3, 4, 5, 9)
#

# my_var = input("Enter a number: ")
# try:
#     my_int = int(my_var)
#     print(my_int)
# except ValueError as e:
#     print("Enter a number")
# except NameError as e:
#     print("Wrong variable name")
# else:
#     print("Without exceptions")
# finally:
#     print("Here with or without exceptions")

#homework
def your_func(*args):
    if len(args) == 0:
        return 0

    sum = 0
    for i in args:
        if(type(i) is int):
            sum += i
    return sum

# print(your_func(1, 5, -3, 'abc', [12, 56, 'cad']))
#
# print(your_func())
#
# print(your_func(2, 4, 'abc'))


def func():
    integer = input("Enter a number: ")
    try:
        my_integer = int(integer)
        print(my_integer)
    except ValueError as e:
        print(int("0"))

# func()



