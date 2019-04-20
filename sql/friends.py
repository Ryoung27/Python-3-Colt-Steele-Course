import sqlite3
conn = sqlite3.connect("my_friends.db")

#SELECT
#INSERT
#CREATE CURSOR OBJECT
c = conn.cursor()
#EXECUTE SOME SQL
c.execute("CREATE TABLE friends (first_name TEXT, last_name TEXT closeness INTEGER);")
#COMMIT CHANGES
conn.commit()
conn.close()