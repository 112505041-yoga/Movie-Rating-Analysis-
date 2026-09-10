-- =====================================================
-- Query 1: Average Rating Per Movie
-- =====================================================
USE movielens;

SELECT
    m.movieId,
    m.title,
    ROUND(AVG(r.rating), 2) AS avg_rating,
    COUNT(r.rating) AS total_ratings
FROM ratings r
JOIN movies m ON r.movieId = m.movieId
GROUP BY m.movieId, m.title
ORDER BY avg_rating DESC
LIMIT 20;
