-- lists all Comedy shows in the database hbtn_0d_tvshows.
SELECT tv_shows.title
    FROM tv_genres INNER JOIN tv_show_genres sh
    ON tv_genres.name = 'Comedy' AND tv_genres.id = sh.genre_id
    INNER JOIN tv_shows ON tv_shows.id = sh.show_id
    ORDER BY tv_shows.title ASC;
