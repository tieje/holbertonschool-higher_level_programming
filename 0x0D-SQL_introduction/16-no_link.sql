-- list all records of second_table
-- don't list rows without a name value
-- display in order of of score
-- display score then name
-- list in descending score
SELECT score, name
FROM second_table
WHERE
    name IS NOT NULL
ORDER BY score
DESC;
