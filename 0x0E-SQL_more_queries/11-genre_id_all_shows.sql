-- lists all shows contained in the database hbtn_0d_tvshows.
SELECT sh.title, g.genre_id
    FROM tv_shows sh LEFT JOIN tv_show_genres g ON sh.id = g.show_id
    ORDER BY sh.title ASC, g.genre_id ASC;
