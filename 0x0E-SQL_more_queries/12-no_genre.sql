-- List all shows
SELECT tv_shows.title AS title, tv_show_genres.genre_id AS genre_id
FROM tv_shows
LEFT JOIN tv_show_genres
WHERE tv_show_genres.show_id is NULL
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id;