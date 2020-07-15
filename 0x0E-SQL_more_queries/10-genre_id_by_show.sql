-- List shows
SELECT tv_shows.title AS title, tv_show_genres.genre_id AS genre.id
FROM tv_shows JOIN tv_show_genres
WHERE tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id;