-- list all DEXTER
SELECT tv_genres.name
FROM tv_shows
JOIN tv_show_genres
ON tv_shows.title = 'Dexter' AND tv_shows.id = tv_show_genres.show_id
INNER JOIN tv_genres
ON tv_shows.id = tv_show_genres.show_id
WHERE tv_genres.id = tv_show_genres.genre_id
ORDER BY tv_genres.name;