-- lists all cities
SELECT
    cities.id,
    cities.name,
    states.name
FROM
    cities,
JOIN states
    ON cities.state_id = state.id
ORDER BY cities.id ASC;
