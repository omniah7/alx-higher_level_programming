-- lists all shows contained in hbtn_0d_tvshows that have at least one genre linked.
SELECT sh.title, g.genre_id
    FROM tv_shows sh INNER JOIN tv_show_genres g ON sh.id = g.show_id
    ORDER BY sh.title ASC, g.genre_id ASC;
