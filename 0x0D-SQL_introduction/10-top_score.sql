-- list all records name and score of second_table in order of  of greatest score
SELECT
    st.score,
    st.name
FROM second_table st
ORDER BY st.score
DESC;
