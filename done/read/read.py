# f =open("text.txt")

# print(f)

# print(f.read())

# # print(f.seek(1))
# # file.read()

# f.closed()

with open("text.txt") as f:
    data = f.read()
    print(data)

with open("haiku.txt", "w") as r:
    r.write("Writing files is interesting.\n")
    r.write("One more time.")

with open("haiku.txt") as r:
    difdata = r.read()
    print(difdata)

with open("haiku.txt", "r+") as r:
    r.write("Look a different line.\n")

def copy(file_name, new_file_name):
    with open(file_name) as file:
        text = file.read()

    with open(new_file_name, "w") as new_file:
        new_file.write(text)

copy("text.txt", "new.txt")