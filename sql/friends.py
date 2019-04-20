import sqlite3
conn = sqlite3.connect("my_friends.db")

#SELECT
#INSERT
#CREATE CURSOR OBJECT
c = conn.cursor()
#EXECUTE SOME SQL
# c.execute("CREATE TABLE friends (first_name TEXT, last_name TEXT, closeness INTEGER);")
# insert_query = '''INSERT INTO friends VALUES ('Merriwether', 'Lewis', 7)'''

# form_first = "Dana"

#BETTER way
data = ("Steve", "Irwin", 9)
query = f"INSERT INTO friends VALUES (?,?,?)"

c.execute(query, data)
#COMMIT CHANGES
conn.commit()
conn.close()