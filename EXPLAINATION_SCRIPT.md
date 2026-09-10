# How to Explain This Project to Your Teacher
## Step-by-Step Presentation Script

---

## PART 1: Introduction (2 minutes)

**YOGANANTH S speaks:**

> "Good morning/afternoon ma'am/sir. We are Yogananth S (112505041) and Sudharsan R (112505032) from MCA department.
>
> Our project is **'Movie Rating Analysis Using Hadoop'**.
>
> The objective of our project is to analyze a large movie rating dataset using Hadoop's distributed computing framework. We used **MapReduce** for low-level data processing and **Apache Hive** for SQL-based querying.
>
> We used the **MovieLens dataset** from GroupLens Research which contains:
> - 9,742 movies
> - 100,836 ratings
> - 610 users
> - 19 genres"

---

## PART 2: Dataset Explanation (1 minute)

**Show dataset folder:**

> "Our dataset has two CSV files:
> - **movies.csv** - Contains movie ID, title, and genres
> - **ratings.csv** - Contains user ID, movie ID, rating (0.5 to 5.0), and timestamp
>
> This is real-world data that is commonly used for big data analytics projects."

---

## PART 3: Project Structure (2 minutes)

**YOGANANTH S speaks:**

> "The project has 4 main components:
> 1. **dataset/** - Raw data files
> 2. **mapreduce/** - 6 Python scripts for MapReduce processing
> 3. **hive/** - 11 Hive SQL queries for analysis
> 4. **output/** - Generated results"

---

## PART 4: MapReduce Explanation (3 minutes)

**YOGANANTH S speaks:**

> "I worked on the MapReduce part. We created 6 MapReduce jobs using Python Streaming:
>
> **Job 1: Average Rating Per Movie**
> - Mapper reads ratings.csv, emits (movieId, rating)
> - Reducer computes average for each movie
>
> **Job 2: Top Rated Movies**
> - Filters movies with minimum 50 ratings
> - Shows top 20 highest rated movies
>
> **Job 3: Most Rated Movies**
> - Counts total ratings per movie
> - Shows most popular movies by rating count
>
> **Job 4: Genre-wise Analysis**
> - Splits pipe-delimited genres
> - Computes average rating per genre
>
> **Job 5: User Activity Analysis**
> - Shows statistics per user
> - Top 30 most active users
>
> **Job 6: Rating Distribution**
> - Shows count of each rating value
> - Displays percentage distribution"

**Show code on screen:**

> "Here is a sample mapper and reducer code..."

---

## PART 5: Hive Explanation (3 minutes)

**SUDHARSAN R speaks:**

> "I worked on the Hive part. We created 11 Hive queries:
>
> First, we created two tables:
> - **movies** table with movieId, title, genres
> - **ratings** table with userId, movieId, rating, timestamp
>
> Then we ran analytical queries:
>
> 1. **Average Rating Per Movie** - Uses GROUP BY and AVG
> 2. **Top Rated Movies** - Adds HAVING COUNT >= 50
> 3. **Most Rated Movies** - Orders by COUNT descending
> 4. **Genre-wise Analysis** - Uses LATERAL VIEW explode() to split genres
> 5. **User Activity** - Shows per-user statistics
> 6. **Rating Distribution** - Count and percentage per rating
> 7. **Year-wise Trends** - Extracts year from movie title
> 8. **Top Genres by Count** - Most popular genres
> 9. **Consistent High-Rated Movies** - Uses STDDEV for consistency
> 10. **User-Genre Preference** - Shows which genres each user likes"

**Show Hive query on screen:**

> "Here is the Hive query for genre-wise analysis using LATERAL VIEW..."

---

## PART 6: Show Results (2 minutes)

**YOGANANTH S speaks:**

> "Let me show you the actual results from our analysis:
>
> **Top Rated Movie:** Shawshank Redemption with 4.43 average rating
>
> **Highest Rated Genre:** Film-Noir with 3.92 average
>
> **Most Popular Genre:** Drama with 41,928 ratings
>
> **Most Common Rating:** 4.0 stars (26.60% of all ratings)
>
> **Average Rating:** 3.50 across all movies
>
> **Most Active User:** User 414 with 2,698 ratings"

**Show output files:**

> "Here are the output files with actual results..."

---

## PART 7: How to Run (2 minutes)

**Show terminal/screen:**

> "Let me demonstrate how to run the project:
>
> **Step 1: Start Hadoop**
> ```
> start-dfs.sh
> start-yarn.sh
> ```
>
> **Step 2: Upload data to HDFS**
> ```
> hdfs dfs -mkdir -p /user/movielens/data
> hdfs dfs -put dataset/*.csv /user/movielens/data/
> ```
>
> **Step 3: Run MapReduce jobs**
> ```
> bash mapreduce/run_all_jobs.sh
> ```
>
> **Step 4: Run Hive queries**
> ```
> hive -f hive/01_create_tables.hql
> ```"

---

## PART 8: Conclusion (1 minute)

**SUDHARSAN R speaks:**

> "In conclusion, our project successfully demonstrates:
>
> 1. How to use Hadoop for big data analytics
> 2. MapReduce for custom data processing
> 3. Hive for SQL-based querying
> 4. Real-world analysis of movie rating data
>
> Key findings:
> - Drama and Comedy are most popular genres
> - Film-Noir gets highest average ratings
> - Most ratings are 4.0 stars
> - Power users contribute many ratings
>
> Thank you. We are ready for any questions."

---

## PART 9: Q&A Preparation

### Likely Questions and Answers:

**Q: Why did you use both MapReduce and Hive?**
> "MapReduce gives low-level control for custom processing, while Hive provides SQL-like simplicity. Using both shows we understand different approaches to big data processing."

**Q: What is LATERAL VIEW explode() in Hive?**
> "It splits a delimited string into multiple rows. We used it to split pipe-delimited genres like 'Action|Comedy' into separate rows for analysis."

**Q: How does Hadoop distribute the data?**
> "HDFS splits files into 128MB blocks and distributes them across DataNodes. MapReduce processes data where it is stored, reducing network transfer."

**Q: What is the difference between Mapper and Reducer?**
> "Mapper processes input data and emits key-value pairs. Reducer groups by key and performs aggregation like sum, average, count."

**Q: What is STDDEV in Job 9?**
> "Standard deviation measures rating consistency. Low STDDEV means users give similar ratings, high STDDEV means ratings vary widely."

**Q: How would this scale to larger datasets?**
> "Hadoop automatically distributes processing across cluster nodes. For millions of ratings, we would add more DataNodes to the cluster."

---

## Tips for Presentation

1. **Speak clearly and confidently**
2. **Show code on screen** while explaining
3. **Run a live demo** if possible
4. **Point to specific files** while explaining
5. **Know your role** - Yogananth: MapReduce, Sudharsan: Hive
6. **Practice** the timing (15-20 minutes total)
7. **Be ready for questions** about Hadoop, MapReduce, Hive

---

## Time Allocation

| Section | Duration | Speaker |
|---------|----------|---------|
| Introduction | 2 min | YOGANANTH S |
| Dataset | 1 min | YOGANANTH S |
| Project Structure | 2 min | YOGANANTH S |
| MapReduce | 3 min | YOGANANTH S |
| Hive | 3 min | SUDHARSAN R |
| Results | 2 min | YOGANANTH S |
| How to Run | 2 min | YOGANANTH S |
| Conclusion | 1 min | SUDHARSAN R |
| Q&A | 5 min | Both |
| **Total** | **~20 min** | |
