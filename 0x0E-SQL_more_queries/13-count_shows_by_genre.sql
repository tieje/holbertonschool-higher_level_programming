-- list all genres and diplay number of shows linked to each
SELECT
    tv_genres.name genre,
    COUNT(tv_show_genres.show_id) number_of_shows
FROM tv_show_genres INNER JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
GROUP BY tv_show_genres.genre_id
ORDER BY number_of_shows DESC;
