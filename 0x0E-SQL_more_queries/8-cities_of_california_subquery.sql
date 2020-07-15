-- list all the cities of a particular state
SELECT id, name FROM cities WHERE (SELECT id FROM states WHERE name="California") ORDER BY id ASC;