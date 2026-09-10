-- =====================================================
-- Query 5: User Activity Analysis
-- =====================================================
USE movielens;

SELECT
    r.userId,
    COUNT(*) AS total_ratings,
    ROUND(AVG(r.rating), 2) AS avg_rating,
    MIN(r.rating) AS min_rating,
    MAX(r.rating) AS max_rating,
    COUNT(DISTINCT r.movieId) AS unique_movies_rated
FROM ratings r
GROUP BY r.userId
ORDER BY total_ratings DESC
LIMIT 30;
