-- =====================================================
-- Movie Rating Analysis - Hive Table Creation & Loading
-- =====================================================

-- Create database
CREATE DATABASE IF NOT EXISTS movielens;
USE movielens;

-- Drop tables if they exist
DROP TABLE IF EXISTS movies;
DROP TABLE IF EXISTS ratings;

-- Create movies table
CREATE TABLE movies (
    movieId INT,
    title STRING,
    genres STRING
)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
ESCAPED BY '"'
LINES TERMINATED BY '\n'
STORED AS TEXTFILE
TBLPROPERTIES ("skip.header.line.count"="1");

-- Create ratings table
CREATE TABLE ratings (
    userId INT,
    movieId INT,
    rating DOUBLE,
    timestamp BIGINT
)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
STORED AS TEXTFILE
TBLPROPERTIES ("skip.header.line.count"="1");

-- Load data from HDFS
-- First upload CSV files to HDFS:
--   hdfs dfs -mkdir -p /user/movielens/data
--   hdfs dfs -put dataset/movies.csv /user/movielens/data/
--   hdfs dfs -put dataset/ratings.csv /user/movielens/data/

LOAD DATA INPATH '/user/movielens/data/movies.csv'
INTO TABLE movies;

LOAD DATA INPATH '/user/movielens/data/ratings.csv'
INTO TABLE ratings;

-- Verify data loaded
SELECT 'Movies count:' AS info, COUNT(*) AS cnt FROM movies
UNION ALL
SELECT 'Ratings count:', COUNT(*) FROM ratings;

-- Sample data
SELECT * FROM movies LIMIT 10;
SELECT * FROM ratings LIMIT 10;
