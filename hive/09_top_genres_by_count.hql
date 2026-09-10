-- =====================================================
-- Query 8: Top 10 Genres by Number of Ratings
-- =====================================================
USE movielens;

SELECT
    genre,
    COUNT(*) AS total_ratings,
    COUNT(DISTINCT r.movieId) AS unique_movies,
    ROUND(AVG(r.rating), 2) AS avg_rating
FROM ratings r
JOIN movies m ON r.movieId = m.movieId
LATERAL VIEW explode(split(m.genres, '\\|')) genre_table AS genre
WHERE genre != '(no genres listed)'
GROUP BY genre
ORDER BY total_ratings DESC
LIMIT 10;
