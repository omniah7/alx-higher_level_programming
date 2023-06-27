-- lists all shows, and all genres linked to that show, from the database hbtn_0d_tvshows.
SELECT tv_shows.title, tv_genres.name
    FROM tv_genres INNER JOIN tv_show_genres sh
    ON tv_genres.id = sh.genre_id
    RIGHT JOIN tv_shows ON tv_shows.id = sh.show_id
    ORDER BY tv_shows.title ASC, tv_genres.name ASC;
