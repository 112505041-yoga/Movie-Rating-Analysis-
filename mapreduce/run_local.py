#!/usr/bin/env python3
"""
Local runner - processes the real dataset and generates all output files.
Simulates MapReduce pipeline without Hadoop.
"""
import csv
import os
from collections import defaultdict

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATASET = os.path.join(BASE, "dataset")
OUTPUT = os.path.join(BASE, "output")

os.makedirs(OUTPUT, exist_ok=True)

# ============================================================
# Load Data
# ============================================================
print("Loading dataset...")

movies = {}
with open(os.path.join(DATASET, "movies.csv"), "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        movies[row["movieId"]] = {"title": row["title"], "genres": row["genres"]}

ratings = []
with open(os.path.join(DATASET, "ratings.csv"), "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        ratings.append({
            "userId": int(row["userId"]),
            "movieId": row["movieId"],
            "rating": float(row["rating"]),
            "timestamp": int(row["timestamp"])
        })

print(f"Loaded {len(movies)} movies and {len(ratings)} ratings.\n")

# ============================================================
# Job 1: Average Rating Per Movie
# ============================================================
print("[Job 1] Average Rating Per Movie...")
movie_ratings = defaultdict(list)
for r in ratings:
    movie_ratings[r["movieId"]].append(r["rating"])

job1_results = []
for mid, rlist in movie_ratings.items():
    avg = sum(rlist) / len(rlist)
    job1_results.append((mid, avg, len(rlist)))

job1_results.sort(key=lambda x: (-x[1], -x[2]))

with open(os.path.join(OUTPUT, "01_avg_rating_per_movie.txt"), "w", encoding="utf-8") as f:
    f.write("=" * 50 + "\n")
    f.write(" MapReduce Job 1: Average Rating Per Movie\n")
    f.write("=" * 50 + "\n")
    f.write(f"{'movieId':<10}{'avg_rating':<14}{'total_ratings':<15}{'title'}\n")
    f.write("-" * 90 + "\n")
    for mid, avg, cnt in job1_results[:20]:
        title = movies.get(mid, {}).get("title", "Unknown")
        f.write(f"{mid:<10}{avg:<14.2f}{cnt:<15}{title}\n")
print(f"  -> Top 20 saved to output/01_avg_rating_per_movie.txt")

# ============================================================
# Job 2: Top 20 Rated Movies (min 50 ratings)
# ============================================================
print("[Job 2] Top Rated Movies (min 50 ratings)...")
job2_results = [(mid, avg, cnt) for mid, avg, cnt in job1_results if cnt >= 50]

with open(os.path.join(OUTPUT, "02_top_rated_movies.txt"), "w", encoding="utf-8") as f:
    f.write("=" * 50 + "\n")
    f.write(" MapReduce Job 2: Top 20 Highest Rated Movies\n")
    f.write(" (minimum 50 ratings required)\n")
    f.write("=" * 50 + "\n")
    f.write(f"{'movieId':<10}{'avg_rating':<14}{'total_ratings':<15}{'title'}\n")
    f.write("-" * 90 + "\n")
    for mid, avg, cnt in job2_results[:20]:
        title = movies.get(mid, {}).get("title", "Unknown")
        f.write(f"{mid:<10}{avg:<14.2f}{cnt:<15}{title}\n")
print(f"  -> Top 20 saved to output/02_top_rated_movies.txt")

# ============================================================
# Job 3: Most Rated Movies (by count)
# ============================================================
print("[Job 3] Most Rated Movies...")
job3_results = [(mid, cnt) for mid, avg, cnt in job1_results]
job3_results.sort(key=lambda x: -x[1])

with open(os.path.join(OUTPUT, "03_most_rated_movies.txt"), "w", encoding="utf-8") as f:
    f.write("=" * 50 + "\n")
    f.write(" MapReduce Job 3: Top 20 Most Rated Movies\n")
    f.write(" (by number of ratings)\n")
    f.write("=" * 50 + "\n")
    f.write(f"{'movieId':<10}{'total_ratings':<15}{'title'}\n")
    f.write("-" * 80 + "\n")
    for mid, cnt in job3_results[:20]:
        title = movies.get(mid, {}).get("title", "Unknown")
        f.write(f"{mid:<10}{cnt:<15}{title}\n")
print(f"  -> Top 20 saved to output/03_most_rated_movies.txt")

# ============================================================
# Job 4: Genre-wise Average Rating
# ============================================================
print("[Job 4] Genre-wise Analysis...")
genre_ratings = defaultdict(list)
for r in ratings:
    mid = r["movieId"]
    if mid in movies:
        genres = movies[mid]["genres"].split("|")
        for g in genres:
            g = g.strip()
            if g and g != "(no genres listed)":
                genre_ratings[g].append(r["rating"])

job4_results = []
for genre, rlist in genre_ratings.items():
    avg = sum(rlist) / len(rlist)
    job4_results.append((genre, avg, len(rlist)))

job4_results.sort(key=lambda x: (-x[1], -x[2]))

with open(os.path.join(OUTPUT, "04_genre_wise_analysis.txt"), "w", encoding="utf-8") as f:
    f.write("=" * 55 + "\n")
    f.write(" MapReduce Job 4: Genre-wise Average Rating Analysis\n")
    f.write("=" * 55 + "\n")
    f.write(f"{'genre':<18}{'avg_rating':<14}{'total_ratings':<15}{'unique_movies'}\n")
    f.write("-" * 70 + "\n")
    for genre, avg, cnt in job4_results:
        unique_movies = len(set(mid for r in ratings if mid in movies and genre in movies[mid]["genres"].split("|")))
        f.write(f"{genre:<18}{avg:<14.2f}{cnt:<15}{unique_movies}\n")
print(f"  -> Saved to output/04_genre_wise_analysis.txt")

# ============================================================
# Job 5: User Activity Analysis
# ============================================================
print("[Job 5] User Activity Analysis...")
user_ratings = defaultdict(list)
for r in ratings:
    user_ratings[r["userId"]].append(r["rating"])

job5_results = []
for uid, rlist in user_ratings.items():
    avg = sum(rlist) / len(rlist)
    job5_results.append((uid, len(rlist), avg, min(rlist), max(rlist)))

job5_results.sort(key=lambda x: -x[1])

with open(os.path.join(OUTPUT, "05_user_activity.txt"), "w", encoding="utf-8") as f:
    f.write("=" * 75 + "\n")
    f.write(" MapReduce Job 5: User Activity Analysis (Top 30 Users)\n")
    f.write("=" * 75 + "\n")
    f.write(f"{'userId':<10}{'totalRatings':<15}{'avgRating':<12}{'minRating':<12}{'maxRating':<12}\n")
    f.write("-" * 65 + "\n")
    for uid, total, avg, mn, mx in job5_results[:30]:
        f.write(f"{uid:<10}{total:<15}{avg:<12.2f}{mn:<12}{mx:<12}\n")
    f.write("\n" + "-" * 65 + "\n")
    f.write(f"Total unique users: {len(user_ratings)}\n")
print(f"  -> Top 30 saved to output/05_user_activity.txt")

# ============================================================
# Job 6: Rating Distribution
# ============================================================
print("[Job 6] Rating Distribution...")
rating_dist = defaultdict(int)
for r in ratings:
    rating_dist[r["rating"]] += 1

total = len(ratings)

with open(os.path.join(OUTPUT, "06_rating_distribution.txt"), "w", encoding="utf-8") as f:
    f.write("=" * 50 + "\n")
    f.write(" MapReduce Job 6: Rating Distribution\n")
    f.write("=" * 50 + "\n")
    f.write(f"{'rating':<12}{'count':<12}{'percentage':<12}\n")
    f.write("-" * 40 + "\n")
    for rating in sorted(rating_dist.keys()):
        count = rating_dist[rating]
        pct = (count / total) * 100
        bar = "#" * int(pct)
        f.write(f"{rating:<12}{count:<12}{pct:<12.2f}%  {bar}\n")
    f.write("\n" + "=" * 50 + "\n")
    f.write(f"Total Ratings: {total:,}\n")
    avg_all = sum(r["rating"] for r in ratings) / total
    most_common = max(rating_dist.items(), key=lambda x: x[1])
    f.write(f"Average Rating: {avg_all:.2f}\n")
    f.write(f"Most Common Rating: {most_common[0]} ({most_common[1]:,} times, {most_common[1]*100/total:.1f}%)\n")
print(f"  -> Saved to output/06_rating_distribution.txt")

# ============================================================
# Job 7: Year-wise Trends (Bonus)
# ============================================================
print("[Job 7] Year-wise Movie Trends...")
import re
year_data = defaultdict(lambda: {"movies": set(), "ratings": 0, "total_rating": 0.0})
for r in ratings:
    mid = r["movieId"]
    if mid in movies:
        match = re.search(r'\((\d{4})\)', movies[mid]["title"])
        if match:
            year = match.group(1)
            year_data[year]["movies"].add(mid)
            year_data[year]["ratings"] += 1
            year_data[year]["total_rating"] += r["rating"]

with open(os.path.join(OUTPUT, "07_year_wise_trends.txt"), "w", encoding="utf-8") as f:
    f.write("=" * 75 + "\n")
    f.write(" Hive Query 7: Year-wise Movie Release and Rating Trends\n")
    f.write("=" * 75 + "\n")
    f.write(f"{'year':<8}{'movies':<10}{'ratings':<12}{'avg_rating':<12}\n")
    f.write("-" * 45 + "\n")
    for year in sorted(year_data.keys()):
        d = year_data[year]
        avg = d["total_rating"] / d["ratings"] if d["ratings"] > 0 else 0
        f.write(f"{year:<8}{len(d['movies']):<10}{d['ratings']:<12}{avg:<12.2f}\n")
print(f"  -> Saved to output/07_year_wise_trends.txt")

# ============================================================
# Summary Stats
# ============================================================
print("\n" + "=" * 50)
print(" ALL JOBS COMPLETED SUCCESSFULLY!")
print("=" * 50)
print(f"\nDataset Summary:")
print(f"  Total Movies:  {len(movies):,}")
print(f"  Total Ratings: {len(ratings):,}")
print(f"  Total Users:   {len(user_ratings):,}")
print(f"  Total Genres:  {len(genre_ratings):,}")
print(f"  Rating Range:  0.5 - 5.0")
print(f"  Avg Rating:    {sum(r['rating'] for r in ratings)/len(ratings):.2f}")
print(f"\nOutput files saved to: {OUTPUT}")
