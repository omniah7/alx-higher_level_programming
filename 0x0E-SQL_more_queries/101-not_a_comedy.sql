-- lists all shows without the genre Comedy in the database hbtn_0d_tvshows.
SELECT tv_shows.title
    FROM tv_genres INNER JOIN tv_show_genres sh
    ON tv_genres.name = 'Comedy' AND tv_genres.id = sh.genre_id
    RIGHT JOIN tv_shows ON tv_shows.id = sh.show_id
    WHERE sh.show_id IS NULL
    ORDER BY tv_shows.title ASC;
