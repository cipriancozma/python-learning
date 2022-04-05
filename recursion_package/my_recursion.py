
#sum of all numbers from 0 to n
def recursive(num):
    if num == 0:
        return 0

    if num > 0:
        return num + recursive(num - 1)


# sum of all even numbers from 0 to n
def recursive_even(num):
    if num == 0:
        return 0

    if not num % 2 ==0:
        return recursive_even(num - 1)
    else:
        return num + recursive_even(num - 1)


#sum of odd numbers
def recursive_odd(num):
    if num == 0:
        return 0

    if not num % 3 == 0:
        return recursive_odd(num - 1)
    else:
        return num + recursive_odd(num - 1)

