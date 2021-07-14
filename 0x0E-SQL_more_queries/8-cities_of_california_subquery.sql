-- list all cities of CA in hbtn_0d_usa db
SELECT
    id,
    name
FROM
    cities c,
    states s
WHERE
    s.state_id = c.state_id
    s.name = "California";
ORDER BY id ASC;
