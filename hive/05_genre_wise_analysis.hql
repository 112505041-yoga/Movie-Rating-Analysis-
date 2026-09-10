-- =====================================================
-- Query 4: Genre-wise Average Rating Analysis
-- Uses lateral view to explode pipe-delimited genres
-- =====================================================
USE movielens;

SELECT
    genre,
    ROUND(AVG(r.rating), 2) AS avg_rating,
    COUNT(*) AS total_ratings,
    COUNT(DISTINCT r.movieId) AS unique_movies
FROM ratings r
JOIN movies m ON r.movieId = m.movieId
LATERAL VIEW explode(split(m.genres, '\\|')) genre_table AS genre
WHERE genre != '(no genres listed)'
GROUP BY genre
ORDER BY avg_rating DESC;
