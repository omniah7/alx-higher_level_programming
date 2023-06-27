-- uses the hbtn_0d_tvshows database to list all genres not linked to the show Dexter
SELECT tv_genres.name
    FROM tv_shows INNER JOIN tv_show_genres sh
    ON tv_shows.title = 'Dexter' AND tv_shows.id = sh.show_id
    RIGHT JOIN tv_genres ON tv_genres.id = sh.genre_id
    WHERE sh.genre_id IS NULL
    ORDER BY tv_genres.name ASC;
