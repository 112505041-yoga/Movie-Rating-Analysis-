-- =====================================================
-- Query 3: Most Rated Movies (by number of ratings)
-- =====================================================
USE movielens;

SELECT
    m.movieId,
    m.title,
    COUNT(r.rating) AS total_ratings,
    ROUND(AVG(r.rating), 2) AS avg_rating
FROM ratings r
JOIN movies m ON r.movieId = m.movieId
GROUP BY m.movieId, m.title
ORDER BY total_ratings DESC
LIMIT 20;
