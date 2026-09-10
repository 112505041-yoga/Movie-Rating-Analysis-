#!/bin/bash
# =====================================================
# Movie Rating Analysis - MapReduce Job Runner
# Run this script from the Hadoop environment
# =====================================================

HADOOP_CMD="hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-*.jar"
RATINGS_PATH="/user/movielens/ratings.csv"
MOVIES_PATH="/user/movielens/movies.csv"
OUTPUT_BASE="/user/movielens/output"

echo "============================================="
echo " Movie Rating Analysis - MapReduce Jobs"
echo "============================================="

# --- Job 1: Average Rating Per Movie ---
echo ""
echo "[Job 1] Average Rating Per Movie..."
hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-*.jar \
    -D mapreduce.input.fileinputformat.split.minsize=134217728 \
    -files mapreduce/01_average_rating_per_movie.py \
    -mapper "python 01_average_rating_per_movie.py" \
    -reducer "python 01_average_rating_per_movie.py reduce" \
    -input $RATINGS_PATH \
    -output $OUTPUT_BASE/01_avg_rating \
    -numReduceTasks 1

echo "[Job 1] Done."

# --- Job 2: Top Rated Movies ---
echo ""
echo "[Job 2] Top Rated Movies (min 50 ratings)..."
hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-*.jar \
    -files mapreduce/02_top_rated_movies.py \
    -mapper "python 02_top_rated_movies.py" \
    -reducer "python 02_top_rated_movies.py reduce" \
    -input $RATINGS_PATH \
    -output $OUTPUT_BASE/02_top_rated \
    -numReduceTasks 1

echo "[Job 2] Done."

# --- Job 3: Most Rated Movies ---
echo ""
echo "[Job 3] Most Rated Movies..."
hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-*.jar \
    -files mapreduce/03_most_rated_movies.py \
    -mapper "python 03_most_rated_movies.py" \
    -reducer "python 03_most_rated_movies.py reduce" \
    -input $RATINGS_PATH \
    -output $OUTPUT_BASE/03_most_rated \
    -numReduceTasks 1

echo "[Job 3] Done."

# --- Job 4: Genre-wise Analysis ---
echo ""
echo "[Job 4] Genre-wise Analysis..."
hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-*.jar \
    -files "mapreduce/04_genre_wise_analysis.py,$MOVIES_PATH#movies.csv" \
    -mapper "python 04_genre_wise_analysis.py" \
    -reducer "python 04_genre_wise_analysis.py reduce" \
    -input $RATINGS_PATH \
    -output $OUTPUT_BASE/04_genre_analysis \
    -numReduceTasks 1

echo "[Job 4] Done."

# --- Job 5: User Activity Analysis ---
echo ""
echo "[Job 5] User Activity Analysis..."
hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-*.jar \
    -files mapreduce/05_user_activity_analysis.py \
    -mapper "python 05_user_activity_analysis.py" \
    -reducer "python 05_user_activity_analysis.py reduce" \
    -input $RATINGS_PATH \
    -output $OUTPUT_BASE/05_user_activity \
    -numReduceTasks 1

echo "[Job 5] Done."

# --- Job 6: Rating Distribution ---
echo ""
echo "[Job 6] Rating Distribution..."
hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-*.jar \
    -files mapreduce/06_rating_distribution.py \
    -mapper "python 06_rating_distribution.py" \
    -reducer "python 06_rating_distribution.py reduce" \
    -input $RATINGS_PATH \
    -output $OUTPUT_BASE/06_rating_distribution \
    -numReduceTasks 1

echo "[Job 6] Done."

echo ""
echo "============================================="
echo " All MapReduce Jobs Completed!"
echo "============================================="
echo ""
echo "Output locations:"
echo "  01_avg_rating          - Average rating per movie"
echo "  02_top_rated           - Top 20 highest rated movies"
echo "  03_most_rated          - Most rated movies by count"
echo "  04_genre_analysis      - Genre-wise average ratings"
echo "  05_user_activity       - User activity analysis"
echo "  06_rating_distribution - Rating value distribution"
echo ""
echo "View output with: hdfs dfs -cat $OUTPUT_BASE/<folder>/part-00000"
