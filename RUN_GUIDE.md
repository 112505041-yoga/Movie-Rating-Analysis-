# Quick Run Guide

---

## Step 1: Start Hadoop

```bash
start-dfs.sh
start-yarn.sh
```

Check services are running:
```bash
jps
```
Should show: NameNode, DataNode, ResourceManager, NodeManager

---

## Step 2: Upload Data to HDFS

```bash
hdfs dfs -mkdir -p /user/movielens/data

hdfs dfs -put "E:\Movie Rating Analysis PROJECT MCA\dataset\movies.csv" /user/movielens/data/

hdfs dfs -put "E:\Movie Rating Analysis PROJECT MCA\dataset\ratings.csv" /user/movielens/data/

hdfs dfs -ls /user/movielens/data/
```

---

## Step 3: Run MapReduce Jobs

```bash
cd "E:\Movie Rating Analysis PROJECT MCA"

bash mapreduce/run_all_jobs.sh
```

---

## Step 4: View MapReduce Results

```bash
hdfs dfs -cat /user/movielens/output/01_avg_rating/part-00000
```

---

## Step 5: Run Hive Queries

```bash
hive -f "E:\Movie Rating Analysis PROJECT MCA\hive\01_create_tables.hql"

hive -f "E:\Movie Rating Analysis PROJECT MCA\hive\02_avg_rating_per_movie.hql"

hive -f "E:\Movie Rating Analysis PROJECT MCA\hive\05_genre_wise_analysis.hql"
```

---

## Or Run Locally (No Hadoop Needed)

```bash
cd "E:\Movie Rating Analysis PROJECT MCA"

python mapreduce/run_local.py
```

Results will be saved in `output/` folder.

---

## Common Errors & Fixes

| Error | Fix |
|-------|-----|
| python not found | Use `python3` instead |
| Output exists | `hdfs dfs -rm -r /user/movielens/output/01_avg_rating` |
| Permission denied | `hdfs dfs -chmod -R 777 /user/movielens` |
