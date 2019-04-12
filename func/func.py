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

def number_compare(x, y):
    if x > y:
        print("First is greater.")
    elif x == y:
        print("Equal")
    else:
        print("Second is greater.")

number_compare(10,100)
number_compare(10, 10)
number_compare(100, 10)