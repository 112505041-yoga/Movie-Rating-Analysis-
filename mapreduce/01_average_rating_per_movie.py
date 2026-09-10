#!/usr/bin/env python
"""
MapReduce Job 1: Average Rating Per Movie
Mapper: Emits (movieId, rating)
Reducer: Computes average rating for each movie
"""

import sys

# ---------- MAPPER ----------
def mapper():
    for line in sys.stdin:
        line = line.strip()
        # Skip header
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
    current_movie = None
    total_rating = 0.0
    count = 0

    for line in sys.stdin:
        line = line.strip()
        parts = line.split("\t")
        if len(parts) != 2:
            continue

        movie_id = parts[0]
        try:
            rating = float(parts[1])
        except ValueError:
            continue

        if current_movie == movie_id:
            total_rating += rating
            count += 1
        else:
            if current_movie is not None:
                avg = total_rating / count
                print(f"{current_movie}\t{avg:.2f}\t{count}")
            current_movie = movie_id
            total_rating = rating
            count = 1

    if current_movie is not None:
        avg = total_rating / count
        print(f"{current_movie}\t{avg:.2f}\t{count}")


if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1 and sys.argv[1] == "reduce":
        reducer()
    else:
        mapper()
