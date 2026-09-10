-- =====================================================
-- Query 2: Top 20 Highest Rated Movies (min 50 ratings)
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
HAVING COUNT(r.rating) >= 50
ORDER BY avg_rating DESC
LIMIT 20;
