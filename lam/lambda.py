# def square(num):
#     return num * num
# print(square(9))

square2 = lambda num: num * num
print(square2(9))

# add = lambda a,b: a + bin

cube = lambda a: a **3

print(cube(2))
print(cube(3))
print(cube(4))

def decrement_list(l):
    return list(map(lambda n: n-1, l))

decrement_list([1,2,3])