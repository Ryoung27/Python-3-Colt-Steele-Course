CREATE TABLE dogs (
    name TEXT,
    breed TEXT,
    age INTEGER
);

CREATE TABLE cats (
    name TEXT,
    breed TEXT,
    age INTEGER
);

INSERT INTO table_name (name, breed, age) VALUES
("Blue", "Random", 29);

INSERT INTO table_name (values in table in order) VALUES
(values match the order)

SELECT * FROM table_name

# SELECTING CERTAIN QUERIES
SELECT * FROM dogs
SELECT * FROM dogs WHERE name IS "Piggy";
SELECT * FROM dogs Where breed IS "Husky";
SELECT * FROM dogs WHERE breed IS NOT "chihuahua" and breed IS NOT "PUG" ;
SELECT * FROM dogs where name LIKE "%gg%"

sqlite3.connect9('example.db')