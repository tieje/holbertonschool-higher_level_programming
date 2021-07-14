-- list all cities of CA in hbtn_0d_usa db
SELECT
    id,
    name
FROM
    cities c,
    states s
WHERE
    s.name = "California";
