-- =====================================================
-- Hive Setup & Execution Script
-- Run in Beeline or Hive CLI
-- =====================================================

-- Step 1: Create database and tables
-- Run: hive -f 01_create_tables.hql

-- Step 2: Run all analytical queries
-- hive -f 02_avg_rating_per_movie.hql
-- hive -f 03_top_rated_movies.hql
-- hive -f 04_most_rated_movies.hql
-- hive -f 05_genre_wise_analysis.hql
-- hive -f 06_user_activity.hql
-- hive -f 07_rating_distribution.hql
-- hive -f 08_year_wise_trends.hql
-- hive -f 09_top_genres_by_count.hql
-- hive -f 10_consistent_high_rated.hql
-- hive -f 11_user_genre_preference.hql

-- Step 3: Export results to HDFS
-- INSERT OVERWRITE DIRECTORY '/user/movielens/hive_output/avg_rating'
-- ROW FORMAT DELIMITED FIELDS TERMINATED BY '\t'
-- SELECT ... (query here);

-- Quick commands to run from terminal:
-- hdfs dfs -mkdir -p /user/movielens/hive_output
-- hive -f hive/01_create_tables.hql
-- hive -f hive/02_avg_rating_per_movie.hql
