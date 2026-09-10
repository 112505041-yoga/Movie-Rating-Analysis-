-- =====================================================
-- Query 10: User-Genre Preference Analysis
-- Shows which genres each user prefers
-- =====================================================
USE movielens;

SELECT
    r.userId,
    genre,
    COUNT(*) AS times_rated,
    ROUND(AVG(r.rating), 2) AS avg_rating_given
FROM ratings r
JOIN movies m ON r.movieId = m.movieId
LATERAL VIEW explode(split(m.genres, '\\|')) genre_table AS genre
WHERE genre != '(no genres listed)'
GROUP BY r.userId, genre
HAVING COUNT(*) >= 5
ORDER BY r.userId, avg_rating_given DESC
LIMIT 50;
