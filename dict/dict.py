ronnie = {
    "name": "Richie",
    "writes_python": True,
    "num_of_jobs": 1,
    "favorite_language": "Python",
    "do_not_tell_javascript": "Javascript"
}

another_dict = dict(key="value", name= "Test")

print(another_dict)

user_info = dict(location="Nashville", state="Tennessee", home="Claiborne")
user_two = {
    "name": "Random",
    "last_name": "House",
    "test": 4
}

print(user_info)
print(user_two)

print(user_two['name'])
print(user_info["location"])

artist = {
    "first": "Neil",
    "last": "Young",
}

full_name = artist['first'] + " " + artist['last']
print(full_name)

donations = dict(sam=25.0, lena=88.99, chuck=13.0, linus=99.5, stan=150.0, lisa=50.25, harrison=10.0)

total_donations = 0
for i in donations.values():
    total_donations = total_donations + i
print(total_donations)