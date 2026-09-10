-- =====================================================
-- Query 7: Year-wise Movie Release and Rating Trends
-- Extracts year from title and analyzes trends
-- =====================================================
USE movielens;

SELECT
    CAST regexp_extract(m.title, '\\((\\d{4})\\)', 1) AS release_year,
    COUNT(DISTINCT m.movieId) AS total_movies,
    COUNT(r.rating) AS total_ratings,
    ROUND(AVG(r.rating), 2) AS avg_rating
FROM ratings r
JOIN movies m ON r.movieId = m.movieId
WHERE regexp_extract(m.title, '\\((\\d{4})\\)', 1) != ''
GROUP BY CAST regexp_extract(m.title, '\\((\\d{4})\\)', 1) AS release_year
ORDER BY release_year
LIMIT 40;
