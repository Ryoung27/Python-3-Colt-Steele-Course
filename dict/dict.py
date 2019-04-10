# ronnie = {
#     "name": "Richie",
#     "writes_python": True,
#     "num_of_jobs": 1,
#     "favorite_language": "Python",
#     "do_not_tell_javascript": "Javascript"
# }

# another_dict = dict(key="value", name= "Test")

# print(another_dict)

# user_info = dict(location="Nashville", state="Tennessee", home="Claiborne")
# user_two = {
#     "name": "Random",
#     "last_name": "House",
#     "test": 4
# }

# print(user_info)
# print(user_two)

# print(user_two['name'])
# print(user_info["location"])

# artist = {
#     "first": "Neil",
#     "last": "Young",
# }

# full_name = artist['first'] + " " + artist['last']
# print(full_name)

# donations = dict(sam=25.0, lena=88.99, chuck=13.0, linus=99.5, stan=150.0, lisa=50.25, harrison=10.0)

# total_donations = 0
# for i in donations.values():
#     total_donations = total_donations + i
# print(total_donations)

# from random import choice #DON'T CHANGE!
# food = choice(["cheese pizza", "quiche","morning bun","gummy bear","tea cake"])

# bakery_stock = {
#     "almond croissant" : 12,
#     "toffee cookie": 3,
#     "morning bun": 1,
#     "chocolate chunk cookie": 9,
#     "tea cake": 25
# }

# for food in bakery_stock:
#     print("{} left".format(bakery_stock[food]))
# else:
#     print("We don't have that")

# game_properties = ["current_score", "high_score", "number_of_lives", "items_in_inventory", "power_ups", "ammo", "enemies_on_screen", "enemy_kills", "enemy_kill_streaks", "minutes_played", "notifications", "achievements"]

# initial_game_properties = dict.fromkeys(game_properties, 0)

list1 = ["CA", "NJ", "RI"]
list2 = ["California", "New Jersey", "Rhode Island"]

answer = {list1[i]: list2[i] for i in range(0,3)}
print(answer)
