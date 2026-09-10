#!/usr/bin/env python
"""
MapReduce Job 3: Most Rated Movies (by number of ratings)
Mapper: Emits (movieId, 1)
Reducer: Counts ratings per movie, sorts by count
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
        if len(parts) >= 2:
            movie_id = parts[1]
            print(f"{movie_id}\t1")

# ---------- REDUCER ----------
def reducer():
    movie_count = defaultdict(int)

    for line in sys.stdin:
        line = line.strip()
        parts = line.split("\t")
        if len(parts) != 2:
            continue
        movie_id = parts[0]
        try:
            count = int(parts[1])
            movie_count[movie_id] += count
        except ValueError:
            continue

    # Sort by count descending
    sorted_movies = sorted(movie_count.items(), key=lambda x: -x[1])

    for movie_id, count in sorted_movies[:20]:
        print(f"{movie_id}\t{count}")


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "reduce":
        reducer()
    else:
        mapper()
