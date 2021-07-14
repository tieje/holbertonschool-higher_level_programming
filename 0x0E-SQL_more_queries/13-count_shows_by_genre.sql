-- list all genres and diplay number of shows linked to each
SELECT
    tv_genres.name genre,
    COUNT(tv_show_genres.id) number_of_shows
FROM tv_genres LEFT JOIN tv_show_genres
ON tv_genres.id = tv_show_genres.genre_id
GROUP BY tv_show_genres.genre_id
ORDER BY tv_genres;
