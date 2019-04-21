# nums = []

# x = 0
# for i in range(1, 100):
#     nums.append(i)
#     x = x + i

# print(x)
# print(nums)

# people = ["Hanna","Louisa","Claudia", "Angela","Geoffrey", "aparna"]

# people.pop(0)
# people.insert(0, "Hannah")
# people.pop(4)
# people.insert(4, "Jeffrey")
# people.pop()
# people.append("Aparna")

# print(people)

# sounds = ["super", "cali", "fragil", "istic", "expi", "ali", "docious"]
# results = ""
# for i in sounds:
#     # results = ""
#     results += i
# print(results.upper())

# instructors = []

# instructors.append("Colt")
# instructors.append("Blue")
# instructors.append("Lisa")

# print(instructors)


# task = ['Install Python', 'Learn Python', 'Take a break']
# demo_list = ["a", 1, 45, True]

# print(len(demo_list))

friends = ["Ashley", "Matt", "Michael"]

# print(friends[1])
# print(friends[-2])

# for friends in friends:
#     print(friends)

# friends.append("Chandler")
# print(friends)

# friends.extend(["Ross", "Phoebe"])
# friends.insert(1, ["Monica", "Joey"])
# print(friends)

# friends.remove(["Monica", "Joey"])
# print(friends)

# friends.clear()
# print(friends)

print(friends.index("Matt"))

print(friends.count("Matt"))
print(friends.reverse())
print(friends)
friends.sort()
print(friends)

some_list = ["Goku", "Krillin", "Vegeta", "Yamcha", "Gohan"]

sayians = some_list[0::2]
fodder = some_list[1::2]

print(sayians)
print(fodder)

print(sayians[::-1])