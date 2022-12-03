-- lists all the cities of California that can be found in the database hbtn_0d_usa.
SELECT * FROM cities
WHERE id = (SELECT id from states
WHERE name = 'California')
