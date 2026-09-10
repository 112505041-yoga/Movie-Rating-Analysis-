-- =====================================================
-- Query 9: Movies with Consistently High Ratings
-- Movies rated by 20+ users with avg > 4.0
-- Stddev < 0.5 means consistent ratings
-- =====================================================
USE movielens;

SELECT
    m.movieId,
    m.title,
    m.genres,
    ROUND(AVG(r.rating), 2) AS avg_rating,
    ROUND(STDDEV(r.rating), 2) AS rating_stddev,
    COUNT(r.rating) AS total_ratings
FROM ratings r
JOIN movies m ON r.movieId = m.movieId
GROUP BY m.movieId, m.title, m.genres
HAVING COUNT(r.rating) >= 20
   AND AVG(r.rating) >= 4.0
   AND STDDEV(r.rating) < 0.5
ORDER BY avg_rating DESC, rating_stddev ASC
LIMIT 20;
