#!/usr/bin/env python
"""
MapReduce Job 2: Top 20 Highest Rated Movies (with minimum 50 ratings)
Mapper: Emits (movieId, rating)
Reducer: Computes average, filters by min ratings, sorts top 20
"""

import sys
from collections import defaultdict

# ---------- MAPPER ----------
def mapper():
    for line in sys.stdin:
        line = line.strip()
        if line.startswith("userId"):
            continue
        parts = line.split(",")
        if len(parts) >= 3:
            movie_id = parts[1]
            try:
                rating = float(parts[2])
                print(f"{movie_id}\t{rating}")
            except ValueError:
                continue

# ---------- REDUCER ----------
def reducer():
    movie_ratings = defaultdict(list)

    for line in sys.stdin:
        line = line.strip()
        parts = line.split("\t")
        if len(parts) != 2:
            continue
        movie_id = parts[0]
        try:
            rating = float(parts[1])
            movie_ratings[movie_id].append(rating)
        except ValueError:
            continue

    # Filter movies with at least 50 ratings and compute average
    results = []
    for movie_id, ratings in movie_ratings.items():
        if len(ratings) >= 50:
            avg = sum(ratings) / len(ratings)
            results.append((movie_id, avg, len(ratings)))

    # Sort by average rating descending
    results.sort(key=lambda x: (-x[1], -x[2]))

    # Print top 20
    for movie_id, avg, count in results[:20]:
        print(f"{movie_id}\t{avg:.2f}\t{count}")


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "reduce":
        reducer()
    else:
        mapper()
