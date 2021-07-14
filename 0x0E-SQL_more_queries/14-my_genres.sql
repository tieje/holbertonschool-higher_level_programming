-- list all genres of Dexter
SELECT
    tv_genres.name name
FROM tv_genres INNER JOIN tv_shows
ON tv_genres.id = tv_shows.genre_id
WHERE tv_shows.title = "Dexter"
ORDER BY name;
