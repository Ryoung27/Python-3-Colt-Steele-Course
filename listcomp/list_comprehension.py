name = ["Elie", "Tim", "Matt"]
answer2 = [i[::-1].lower() for i in name]
answer = [i[0] for i in name]
print(answer)
print(answer2)

numbers = [1,2,3,4,5,6]
answer2 = [num for num in numbers if num % 2 == 0]
print(answer2)

test = [1,2,3,4]
test2 = [3,4,5,6]

answer3 = []
for x in test:
    if x in test2:
        answer3.append(x)
print(answer3)

# nums = [1, 2, 3]

# multi_nums = [x*10 for x in nums]

# print(multi_nums)

# name = 'richie'
# big_name = [i.upper() for i in name]
# print(big_name)
# boo_test = [bool(val) for val in [0, [], '', True]]
# print(boo_test)

# nums = [1, 2, 3, 4, 5]
# string_nums = [str(num) for num in nums]
# print(string_nums)

# numbers = [1, 2, 3, 4, 5, 6]

# evens = [num for num in numbers if num % 2 == 0]

# oods = [num for num in numbers if num % 2 != 0]
