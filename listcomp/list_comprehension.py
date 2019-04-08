nums = [1, 2, 3]

multi_nums = [x*10 for x in nums]

print(multi_nums)

name = 'richie'
big_name = [i.upper() for i in name]
print(big_name)
boo_test = [bool(val) for val in [0, [], '', True]]
print(boo_test)

nums = [1, 2, 3, 4, 5]
string_nums = [str(num) for num in nums]
print(string_nums)