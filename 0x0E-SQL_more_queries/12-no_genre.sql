-- lists all shows contained in hbtn_0d_tvshows without a genre linked.
SELECT sh.title, g.genre_id
    FROM tv_shows sh LEFT JOIN tv_show_genres g
    ON sh.id = g.show_id
    WHERE g.show_id IS NULL
    ORDER BY sh.title ASC, g.genre_id ASC;
