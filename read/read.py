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