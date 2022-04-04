# print("Hello Py")

nume = "Popescu"
prenume = "Ionel"

text = f"""
Buna ziua,

Ma numesc {nume} {prenume}.

Bine ati venit!!!
"""
# print(text)

l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(l[4:])

g = l[:]
l[0] = "a"

# print(l)
# print(g)

dictionary = {
    "Name": "Ciprian",
    "Surname": "Ciprian2",
    "age": 22
}

# print(dictionary["Name"])
# print(dictionary.get("age", 17))

s = {1, 2, 3}
c = {1, 2}

# print(c.intersection(s))  #ce e comun intre cele doua seturi

#Homework
#declare a list with some elements

numbers = [7, 8, 9, 2, 3, 1, 4, 10, 5, 6]

#display a ordered list (initial list should remain the same)
numbers_ordered = sorted(numbers)

print("numbers", numbers)
print("numbers ordered", numbers_ordered)

#display a ordered list in a descendent way (initial list should remain the same)
numbers_ordered_descendent = sorted(numbers, reverse=True)
print("numbers ordered descendent", numbers_ordered_descendent)

#even numbers from list
even_numbers = numbers_ordered[1::2]
print("even numbers", even_numbers)

#odd numbers from list
odd_numbers = numbers_ordered[::2]
print("odd numbers", odd_numbers)

#display multiply of 3
multiply_by_3 = numbers_ordered[2::3]
print("multiplies by 3", multiply_by_3)
