import sqlite3
conn = sqlite3.connect("my_friends.db")

#SELECT
#INSERT
#CREATE CURSOR OBJECT
c = conn.cursor()

c.execute("SELECT * FROM friends")
# for results in c:
#     print(results)
print(c.fetchall())
#EXECUTE SOME SQL
# c.execute("CREATE TABLE friends (first_name TEXT, last_name TEXT, closeness INTEGER);")
# insert_query = '''INSERT INTO friends VALUES ('Merriwether', 'Lewis', 7)'''

# form_first = "Dana"

#BETTER way
# data = ("Steve", "Irwin", 9)
# query = f"INSERT INTO friends VALUES (?,?,?)"

# #BULK INSERTION
# people = [
#     ("Roald", "Amundsen", 5),
#     ("Posa", "Rarks", 8),
#     ("Henry", "Hudson", 7),
#     ("Aeil", "Nrmstrong", 7),
#     ("Baneil", "Doone", 10)
# ]

# # c.executemany("INSERT INTO friends VALUES (?,?,?)", people)

# for person in people:
#     c.execute("INSERT INTO friends VALUES (?,?,?)", person)
#     print("INSERTING NOW!")

# c.execute(query, data)
#COMMIT CHANGES
conn.commit()
conn.close()