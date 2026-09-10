# Movie Rating Analysis Using Hadoop

## MCA Group Project

---

## Team Members

| Roll No | Name | Role |
|---------|------|------|
| **112505041** | **YOGANANTH S** | Project Lead & MapReduce Developer |
| **112505032** | **SUDHARSAN R** | Hive Developer & Documentation |

---

## Role Assignments

### YOGANANTH S (112505041) - Project Lead & MapReduce Developer

**Responsibilities:**
- Project planning and coordination
- Designing and implementing all MapReduce jobs
- Data preprocessing and pipeline setup
- Running and testing all MapReduce scripts
- Dataset preparation and analysis

**Tasks Completed:**
1. All 6 MapReduce Python scripts (mapper/reducer)
2. Local execution pipeline (`run_local.py`)
3. Hadoop streaming job runner (`run_all_jobs.sh`)
4. Data analysis and output generation

---

### SUDHARSAN R (112505032) - Hive Developer & Documentation

**Responsibilities:**
- Designing and implementing all Hive queries
- Database schema design
- Writing project documentation
- Creating presentation materials
- Testing Hive queries

**Tasks Completed:**
1. All 11 Hive queries (`.hql` files)
2. Table creation and data loading scripts
3. Project report (`project_report.md`)
4. How to run guide (`HOW_TO_RUN.md`)

---

## Project Structure

```
Movie Rating Analysis PROJECT MCA/
│
├── dataset/                    # Raw data (MovieLens)
│   ├── movies.csv              (9,742 movies)
│   └── ratings.csv             (100,836 ratings)
│
├── mapreduce/                  # MapReduce Scripts (YOGANANTH S)
│   ├── 01_average_rating_per_movie.py
│   ├── 02_top_rated_movies.py
│   ├── 03_most_rated_movies.py
│   ├── 04_genre_wise_analysis.py
│   ├── 05_user_activity_analysis.py
│   ├── 06_rating_distribution.py
│   ├── run_local.py
│   └── run_all_jobs.sh
│
├── hive/                       # Hive Queries (SUDHARSAN R)
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
│
├── output/                     # Generated Results
│   └── 7 output files
│
├── documentation/              # Project Report
│   └── project_report.md
│
└── HOW_TO_RUN.md              # Execution Guide
```

---

## Tools Used

| Tool | Purpose | Used By |
|------|---------|---------|
| Hadoop HDFS | Distributed file storage | Both |
| MapReduce (Python) | Data processing | YOGANANTH S |
| Apache Hive | SQL querying | SUDHARSAN R |
| Python 3 | Script development | Both |
| Git/GitHub | Version control | Both |

---

## Dataset

- **Source:** MovieLens Dataset (GroupLens Research)
- **Movies:** 9,742
- **Ratings:** 100,836
- **Users:** 610
- **Genres:** 19
- **Rating Range:** 0.5 to 5.0

---

## How to Run

### Quick Start
```bash
# 1. Start Hadoop
start-dfs.sh && start-yarn.sh

# 2. Upload data
hdfs dfs -mkdir -p /user/movielens/data
hdfs dfs -put dataset/*.csv /user/movielens/data/

# 3. Run MapReduce jobs
bash mapreduce/run_all_jobs.sh

# 4. Run Hive queries
hive -f hive/01_create_tables.hql
```

See `HOW_TO_RUN.md` for detailed instructions.

---

## Results Summary

| Analysis | Key Finding |
|----------|-------------|
| Top Movie | Shawshank Redemption (4.43 rating) |
| Top Genre | Film-Noir (3.92 avg rating) |
| Most Popular | Drama (41,928 ratings) |
| Most Common Rating | 4.0 (26.60%) |
| Most Active User | User 414 (2,698 ratings) |
| Average Rating | 3.50 |

---

## Declaration

We hereby declare that this project is our original work and has been completed under the guidance of our institution.

| | |
|---|---|
| **YOGANANTH S** | **SUDHARSAN R** |
| Roll No: 112505041 | Roll No: 112505032 |
| MCA | MCA |

---
