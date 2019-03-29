# cash = 19867324678987.99

# print(cash/5)

# x = 100

# dragon = 1

# print(dragon)

# print(dragon + 1)

# just_another_var = dragon * 100

# print(just_another_var)

i = 2

while i < 6:
    print(i)
    i+= 1

i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1

i = 1
while i < 6:
    print(i)
    i += 1

def new_function():
    print("Print this is a function")

new_function()

def another_function(name1, name2, name3):
    print(name1 + name2 + name3)

another_function("Ronnie ", "Richard ", "Young")

def country_func(country = "Norway"):
    print("I am from " + country)

country_func("Canada")
country_func()

def tri_recursion(k):
    if(k>0):
        result = tri_recursion(k-1)
        print(result)
    else:
        result = 0
    return result

tri_recursion(6)

blah_2_blach = 2
print(blah_2_blach)

print(type(None))

age = None
print(age)

city = "Nashville"
price = 2.00
high_score = 100000000
is_having_fun = True


witch_mountain = "/\/\/\/\/\/\/\\"

print(witch_mountain)