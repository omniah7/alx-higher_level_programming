-- uses the hbtn_0d_tvshows database to lists all genres of the show Dexter.
SELECT tv_genres.name
    FROM tv_shows INNER JOIN tv_show_genres sh
    ON tv_shows.title = 'Dexter' AND tv_shows.id = sh.show_id
    INNER JOIN tv_genres ON tv_genres.id = sh.genre_id
    ORDER BY tv_genres.name ASC;
