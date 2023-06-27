-- lists all shows from hbtn_0d_tvshows_rate by their rating.
SELECT tv_shows.title, SUM(r.rate) 'rating'
    FROM tv_shows INNER JOIN tv_show_ratings r
    ON tv_shows.id = r.show_id
    GROUP BY tv_shows.title
    ORDER BY SUM(r.rate) DESC;
