-- lists all records with score >= 10
SELECT
    st.score,
    st.name
FROM second_table st
WHERE 
    st.score >= 10
ORDER BY st.score
DESC;
