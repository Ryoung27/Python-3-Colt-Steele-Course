# def intersection(x, y):
#     new_list = []
#     for i in x:
#         for n in y:
#             if i == n:
#                 new_list.append(i)
#     return new_list

# print(intersection([1,2,3,4],[3,4,5,6,7]))

def reverse_string(string):
    # print("something")
    string[::-1]
    print(string[::-1])
    # string = string[:-1]

reverse_string("Racecar")

# def capitalize(string):
#     return string[:1].upper() + string[1:]
#     # racecar = str()
#     # for i in x:
#     #     if i == x[0]:
#     #         print("inside")
#     #         i.upper()
#     #         racecar = racecar + i
#     #     else:
#     #         racecar=  racecar + i

#     # print(racecar)
# print(capitalize("racecar"))

# def mulitply_even_numbers(a_list):
#     sum = 1
#     for i in a_list:
#         if i % 2 == 0:
#             sum = sum * i
#     print(sum)

# a_list= [1,2,3,4,1,1,1,1,1, 4, 2]
# mulitply_even_numbers(a_list)

# def frequency(a_list, x):
#     count = 0
#     for i in a_list:
#         if i == x:
#             count = count + 1
#     print(count)

# a_list= [1,2,3,4,1,1,1,1,1]

# frequency(a_list, 1)

# def reverse(x):
#     return x[::-1]

# print(reverse("racecar"))


# def is_pali(x):
#     rev = reverse(x)
#     if x == rev:
#         print("It's a palindrome Harry")
#     else:
#         print("Not a palindrome")

# is_pali("racecar")
# is_pali("Jackson")
# def list_manipulation(a_list, command, location, value):
#     if command == 'remove' and location == 'end':
#         del a_list[-1]
#     elif command == 'remove' and location == "beginning":
#         del a_list[0]
#     elif command == "add" and location == "beginning":
#         return a_list.insert(0, value)
#     elif command == "add" and location == "end":
#         return a_list.append(value)

# a_list=[1,2,3,4,5]

# list_manipulation(a_list, "add", "end", 6)
# print(a_list)
# list_manipulation(a_list, "remove", "end", 0)
# print(a_list)
# # def square(num):
#     return num * num

# def multiply(x, y):
#     return x * y


# def square(x):
#     return x * x

# print(square(2))

# from random import random

# def coin_flip():
#     coin = random()
#     if coin > 0.5:
#         return "Heads"
#     else:
#         return "Tails"
# print(coin_flip())


# def print_square_of_7():
#     print(7 * 7)

# print_square_of_7()

# def square_of_10():
#     return(10 * 10)

# ten = square_of_10()
# print(ten)

# def name_of_function():
#     print("Hi")

# def happy_birthday():
#     print("Happy birthday to you.")

# happy_birthday()

# def make_noise():
#     print("hello")

# make_noise()

# def speak_pig():
#     return "oink"

# speak_pig()

# list_even = []
# def generate_evens():
#     for i in range(1,50):
#         if i % 2 == 0:
#             list_even.append(i)
#     print(list_even)

# generate_evens()

# def yell(scream_it):
#     return scream_it.upper()

# print(yell("ahhhh"))

# def speak(animal):
#     if animal == "pig":
#         return "Oink"
#     elif animal == "duck":
#         return "Quack"
#     elif animal == "cat":
#         return "Meow"
#     elif animal == None:
#         animal == "dog"
#     elif animal == "dog":
#         return "Bark"
#     else:
#         return "???"

# print(speak("dog"))
# print(speak("cat"))
# print(speak("dog"))
# print(speak("m"))

# def count_dollar_signs(word):
#     count = 0
#     for char in word:
#         if char == '$':
#             count += 1
#     return count

# # print(count_dollar_signs("$uper $ize"))

# def product(x, y):
#     return(x * y)

# print(product(1, 1))
# print(product(7, 10))

# def week_day(x):
#     if x == 1:
#         return "Sunday"
#     elif x == 2:
#         return "Monday"
#     elif x == 3:
#         return "Tuesday"
#     else:
#         return "None of that."

# print(week_day(2))
# print(week_day(0))

# def last_element(x):
#     for i in x:
#         if i == x[-1]:
#             print(i)
#         else:
#             pass

# last_element([1,2,3,4,5])

# def number_compare(x, y):
#     if x > y:
#         print("First is greater.")
#     elif x == y:
#         print("Equal")
#     else:
#         print("Second is greater.")

# number_compare(10,100)
# number_compare(10, 10)
# number_compare(100, 10)


# def single_letter_count(x, y):
#     count = 0
#     for i in x:
#         if i == y:
#             count += 1
#     print(count)

# single_letter_count("Shazamm", "m")