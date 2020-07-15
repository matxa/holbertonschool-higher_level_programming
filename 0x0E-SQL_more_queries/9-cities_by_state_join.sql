-- List all cities and state
SELECT cities.id AS id, cities.name AS name, states.name AS name FROM cities JOIN states WHERE cities.state_id = states.id ORDER BY cities.id ASC;