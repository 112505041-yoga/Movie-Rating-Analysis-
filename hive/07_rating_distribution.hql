-- =====================================================
-- Query 6: Rating Distribution
-- =====================================================
USE movielens;

SELECT
    rating,
    COUNT(*) AS count,
    ROUND(COUNT(*) * 100.0 / (SELECT COUNT(*) FROM ratings), 2) AS percentage
FROM ratings
GROUP BY rating
ORDER BY rating;
