# Movie Rating Analysis Using Hadoop
## MCA Project Report

---

## 1. Introduction

### 1.1 Project Title
Movie Rating Analysis Using Hadoop Ecosystem (MapReduce & Hive)

### 1.2 Objective
To analyze the MovieLens dataset containing movie ratings using Hadoop's distributed computing framework. The project performs various analytical tasks including computing average ratings, identifying top-rated movies, genre-wise analysis, user behavior analysis, and rating distribution analysis using both MapReduce and Hive.

### 1.3 Dataset
- **Source:** MovieLens Dataset (GroupLens Research)
- **Files:**
  - `movies.csv` — 9,742 movies with movieId, title, and genres
  - `ratings.csv` — 100,836 ratings with userId, movieId, rating (0.5-5.0), and timestamp
  - **Total Users:** 610
  - **Total Genres:** 19
  - **Average Rating:** 3.50

---

## 2. Tools & Technologies

| Technology | Purpose |
|---|---|
| Hadoop HDFS | Distributed file storage |
| MapReduce (Python Streaming) | Data processing via mapper/reducer |
| Apache Hive | SQL-based data querying |
| Python | MapReduce script language |
| Bash | Job orchestration scripts |

---

## 3. Project Structure

```
Movie Rating Analysis PROJECT MCA/
├── dataset/
│   ├── movies.csv            # Movie metadata
│   └── ratings.csv           # User ratings
├── mapreduce/
│   ├── 01_average_rating_per_movie.py
│   ├── 02_top_rated_movies.py
│   ├── 03_most_rated_movies.py
│   ├── 04_genre_wise_analysis.py
│   ├── 05_user_activity_analysis.py
│   ├── 06_rating_distribution.py
│   └── run_all_jobs.sh
├── hive/
│   ├── 01_create_tables.hql
│   ├── 02_avg_rating_per_movie.hql
│   ├── 03_top_rated_movies.hql
│   ├── 04_most_rated_movies.hql
│   ├── 05_genre_wise_analysis.hql
│   ├── 06_user_activity.hql
│   ├── 07_rating_distribution.hql
│   ├── 08_year_wise_trends.hql
│   ├── 09_top_genres_by_count.hql
│   ├── 10_consistent_high_rated.hql
│   ├── 11_user_genre_preference.hql
│   └── run_all_queries.sh
├── output/                   # Sample output results
└── documentation/
    └── project_report.md
```

---

## 4. MapReduce Jobs

### 4.1 Average Rating Per Movie (Job 01)
- **Mapper:** Reads `ratings.csv`, emits `(movieId, rating)`
- **Reducer:** Groups by movieId, computes average rating
- **Output:** movieId, average rating, total count

### 4.2 Top Rated Movies (Job 02)
- **Mapper:** Emits `(movieId, rating)`
- **Reducer:** Aggregates ratings, filters movies with 50+ ratings, sorts by average
- **Output:** Top 20 highest rated movies

### 4.3 Most Rated Movies (Job 03)
- **Mapper:** Emits `(movieId, 1)` for counting
- **Reducer:** Counts ratings per movie, sorts by count
- **Output:** Top 20 most rated movies

### 4.4 Genre-wise Analysis (Job 04)
- **Mapper:** Joins ratings with movie genres from distributed cache, emits `(genre, rating)`
- **Reducer:** Computes average rating per genre
- **Output:** Genre, average rating, total ratings

### 4.5 User Activity Analysis (Job 05)
- **Mapper:** Emits `(userId, rating)`
- **Reducer:** Computes per-user statistics (total, avg, min, max)
- **Output:** User activity summary for top 30 users

### 4.6 Rating Distribution (Job 06)
- **Mapper:** Emits `(rating, 1)`
- **Reducer:** Counts occurrences of each rating value with percentages
- **Output:** Rating distribution with percentages

---

## 5. Hive Analytical Queries

### Q1: Average Rating Per Movie
Computes average rating and total count per movie, ordered by highest rating.

### Q2: Top Rated Movies
Same as Q1 but filters movies with minimum 50 ratings.

### Q3: Most Rated Movies
Shows movies ranked by number of ratings received.

### Q4: Genre-wise Analysis
Uses `LATERAL VIEW explode()` to split pipe-delimited genres and compute per-genre statistics.

### Q5: User Activity
Shows per-user statistics: total ratings, average, min, max, unique movies rated.

### Q6: Rating Distribution
Shows count and percentage for each rating value (0.5 to 5.0).

### Q7: Year-wise Trends
Extracts release year from title and shows movie/rating trends by year.

### Q8: Top Genres by Count
Ranks genres by total number of ratings received.

### Q9: Consistent High-Rated Movies
Finds movies with avg rating >= 4.0, 20+ ratings, and low standard deviation (< 0.5).

### Q10: User-Genre Preference
Shows which genres each user rates most frequently and their average rating per genre.

---

## 6. How to Run

### 6.1 Prerequisites
- Hadoop cluster (single-node or multi-node)
- HDFS configured and running
- Python 2.x or 3.x (for Hadoop Streaming)

### 6.2 Upload Data to HDFS
```bash
hdfs dfs -mkdir -p /user/movielens/data
hdfs dfs -put dataset/movies.csv /user/movielens/data/
hdfs dfs -put dataset/ratings.csv /user/movielens/data/
```

### 6.3 Run MapReduce Jobs
```bash
chmod +x mapreduce/run_all_jobs.sh
bash mapreduce/run_all_jobs.sh
```

### 6.4 Run Hive Queries
```bash
hive -f hive/01_create_tables.hql
hive -f hive/02_avg_rating_per_movie.hql
```

### 6.5 View MapReduce Output
```bash
hdfs dfs -cat /user/movielens/output/01_avg_rating/part-00000
```

---

## 7. Sample Results (Actual Data)

### Top 10 Highest Rated Movies (min 50 ratings)
| Movie | Avg Rating | Count |
|---|---|---|
| Shawshank Redemption, The (1994) | 4.43 | 317 |
| Godfather, The (1972) | 4.29 | 192 |
| Fight Club (1999) | 4.27 | 218 |
| Cool Hand Luke (1967) | 4.27 | 57 |
| Dr. Strangelove (1964) | 4.27 | 97 |
| Rear Window (1954) | 4.26 | 84 |
| Godfather: Part II, The (1974) | 4.26 | 129 |
| Departed, The (2006) | 4.25 | 107 |
| Goodfellas (1990) | 4.25 | 126 |
| Casablanca (1942) | 4.24 | 100 |

### Rating Distribution
| Rating | Count | Percentage |
|---|---|---|
| 0.5 | 1,370 | 1.36% |
| 1.0 | 2,811 | 2.79% |
| 1.5 | 1,791 | 1.78% |
| 2.0 | 7,551 | 7.49% |
| 2.5 | 5,550 | 5.50% |
| 3.0 | 20,047 | 19.88% |
| 3.5 | 13,136 | 13.03% |
| 4.0 | 26,818 | 26.60% |
| 4.5 | 8,551 | 8.48% |
| 5.0 | 13,211 | 13.10% |

### Top 10 Genres by Average Rating
| Genre | Avg Rating | Count |
|---|---|---|
| Film-Noir | 3.92 | 870 |
| War | 3.81 | 4,859 |
| Documentary | 3.80 | 1,219 |
| Crime | 3.66 | 16,681 |
| Drama | 3.66 | 41,928 |
| Mystery | 3.63 | 7,674 |
| Animation | 3.63 | 6,988 |
| IMAX | 3.62 | 4,145 |
| Western | 3.58 | 1,930 |
| Musical | 3.56 | 4,138 |

### Top 5 Most Active Users
| User | Total Ratings | Avg Rating | Min | Max |
|---|---|---|---|---|
| 414 | 2,698 | 3.47 | 1.0 | 5.0 |
| 599 | 2,478 | 3.39 | 0.5 | 5.0 |
| 68 | 2,280 | 3.54 | 1.0 | 5.0 |
| 405 | 2,186 | 3.15 | 0.5 | 5.0 |
| 474 | 2,130 | 3.62 | 1.0 | 5.0 |

---

## 8. Conclusion

The project successfully demonstrates the use of Hadoop ecosystem for big data analytics on movie rating data. MapReduce provides low-level control for custom data processing, while Hive offers SQL-like simplicity for analytical queries. Key findings from the actual dataset analysis:
- **Drama** (41,928 ratings) and **Comedy** (39,053 ratings) are the most popular genres
- **Film-Noir** (3.92), **War** (3.81), and **Documentary** (3.80) receive highest average ratings
- **Horror** (3.26) receives the lowest average ratings
- **4.0** is the most common rating (26.60% of all ratings)
- The average rating across all movies is **3.50**
- User 414 is the most active with 2,698 ratings
- **Shawshank Redemption** tops the highest-rated movies with 4.43 average (317 ratings)

---

## 9. References

1. GroupLens Research - MovieLens Dataset: https://grouplens.org/datasets/movielens/
2. Apache Hadoop Documentation: https://hadoop.apache.org/docs/
3. Apache Hive LanguageManual: https://cwiki.apache.org/confluence/display/Hive/LanguageManual
4. Hadoop Streaming: https://hadoop.apache.org/docs/current/hadoop-streaming/HadoopStreaming.html
