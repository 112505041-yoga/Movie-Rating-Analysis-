# How to Run This Project
## Step-by-Step Guide

---

## Prerequisites

1. **Hadoop installed** (single-node cluster is fine)
   ```bash
   # Check Hadoop is running
   jps
   # Should show: NameNode, DataNode, ResourceManager, NodeManager
   ```

2. **Python installed** (for MapReduce scripts)

3. **Hive installed** (for Hive queries)

---

## Step 1: Start Hadoop Services

```bash
# Start HDFS and YARN
start-dfs.sh
start-yarn.sh

# Verify all services are running
jps
```

---

## Step 2: Upload Data to HDFS

```bash
# Create directory in HDFS
hdfs dfs -mkdir -p /user/movielens/data

# Upload both CSV files
hdfs dfs -put "E:\Movie Rating Analysis PROJECT MCA\dataset\movies.csv" /user/movielens/data/
hdfs dfs -put "E:\Movie Rating Analysis PROJECT MCA\dataset\ratings.csv" /user/movielens/data/

# Verify upload
hdfs dfs -ls /user/movielens/data/
```

---

## Step 3: Run MapReduce Jobs

```bash
# Navigate to project folder
cd "E:\Movie Rating Analysis PROJECT MCA"

# Run all 6 jobs at once
bash mapreduce/run_all_jobs.sh
```

### Or Run Individual Jobs:

```bash
# Job 1: Average Rating Per Movie
hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-*.jar \
    -files mapreduce/01_average_rating_per_movie.py \
    -mapper "python 01_average_rating_per_movie.py" \
    -reducer "python 01_average_rating_per_movie.py reduce" \
    -input /user/movielens/data/ratings.csv \
    -output /user/movielens/output/01_avg_rating \
    -numReduceTasks 1
```

---

## Step 4: View MapReduce Output

```bash
# View any output
hdfs dfs -cat /user/movielens/output/01_avg_rating/part-00000

# Copy output to local machine
hdfs dfs -get /user/movielens/output/01_avg_rating/part-00000 ./output/
```

---

## Step 5: Run Hive Queries

```bash
# Create database and tables
hive -f hive/01_create_tables.hql

# Run all queries one by one
hive -f hive/02_avg_rating_per_movie.hql
hive -f hive/03_top_rated_movies.hql
hive -f hive/04_most_rated_movies.hql
hive -f hive/05_genre_wise_analysis.hql
hive -f hive/06_user_activity.hql
hive -f hive/07_rating_distribution.hql
hive -f hive/08_year_wise_trends.hql
hive -f hive/09_top_genres_by_count.hql
hive -f hive/10_consistent_high_rated.hql
hive -f hive/11_user_genre_preference.hql
```

### Or Run in Beeline:
```bash
beeline -u jdbc:hive2://localhost:10000 -n hadoop

# Then paste queries from .hql files
```

---

## Step 6: Export Hive Results to HDFS

```bash
# Example: Export top rated movies
hive -e "
INSERT OVERWRITE DIRECTORY '/user/movielens/hive_output/top_rated'
ROW FORMAT DELIMITED FIELDS TERMINATED BY '\t'
SELECT m.movieId, m.title, ROUND(AVG(r.rating),2), COUNT(r.rating)
FROM ratings r JOIN movies m ON r.movieId = m.movieId
GROUP BY m.movieId, m.title
HAVING COUNT(r.rating) >= 50
ORDER BY AVG(r.rating) DESC
LIMIT 20;
"

# View exported results
hdfs dfs -cat /user/movielens/hive_output/top_rated/part-00000
```

---

## Quick Summary

| Step | Command |
|------|---------|
| Start Hadoop | `start-dfs.sh && start-yarn.sh` |
| Upload Data | `hdfs dfs -put dataset/*.csv /user/movielens/data/` |
| Run MapReduce | `bash mapreduce/run_all_jobs.sh` |
| Run Hive | `hive -f hive/01_create_tables.hql` |
| View Output | `hdfs dfs -cat /user/movielens/output/01_avg_rating/part-00000` |

---

## Troubleshooting

| Issue | Solution |
|-------|----------|
| `python not found` | Use `python3` instead of `python` |
| `Permission denied` | Run `hdfs dfs -chmod -R 777 /user/movielens` |
| `Output directory exists` | Run `hdfs dfs -rm -r /user/movielens/output/01_avg_rating` |
| `Hive not starting` | Check ` metastore` is running: `nohup hive --service metastore &` |
