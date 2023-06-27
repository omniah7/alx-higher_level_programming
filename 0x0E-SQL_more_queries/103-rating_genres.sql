-- lists all genres in the database hbtn_0d_tvshows_rate by their rating.
SELECT tv_genres.name, SUM(r.rate)
    FROM tv_genres INNER JOIN tv_show_genres sh ON tv_genres.id = sh.genre_id
    INNER JOIN tv_shows ON tv_shows.id = sh.show_id
    INNER JOIN tv_show_ratings r ON r.show_id = sh.show_id
    GROUP BY tv_genres.name
    ORDER BY SUM(r.rate) DESC;
