#!/usr/bin/env python
"""
MapReduce Job 4: Genre-wise Average Rating Analysis
Mapper: Reads both ratings and movies, emits (genre, rating)
Reducer: Computes average rating per genre
"""

import sys
from collections import defaultdict

# ---------- MAPPER ----------
def mapper():
    """Reads ratings.csv from stdin. movies.csv must be pre-loaded via distributed cache."""
    movies = {}

    # Read movie data from distributed cache
    try:
        with open("movies.csv", "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line.startswith("movieId"):
                    continue
                # Handle quoted titles with commas
                parts = line.split(",")
                if len(parts) >= 3:
                    movie_id = parts[0]
                    genres = parts[-1]  # Last field is genres
                    movies[movie_id] = genres
    except FileNotFoundError:
        pass

    # Read ratings from stdin
    for line in sys.stdin:
        line = line.strip()
        if line.startswith("userId"):
            continue
        parts = line.split(",")
        if len(parts) >= 3:
            movie_id = parts[1]
            try:
                rating = float(parts[2])
                if movie_id in movies:
                    genres = movies[movie_id].split("|")
                    for genre in genres:
                        genre = genre.strip()
                        if genre and genre != "(no genres listed)":
                            print(f"{genre}\t{rating}")
            except ValueError:
                continue

# ---------- REDUCER ----------
def reducer():
    genre_ratings = defaultdict(list)

    for line in sys.stdin:
        line = line.strip()
        parts = line.split("\t")
        if len(parts) != 2:
            continue
        genre = parts[0]
        try:
            rating = float(parts[1])
            genre_ratings[genre].append(rating)
        except ValueError:
            continue

    for genre in sorted(genre_ratings.keys()):
        ratings = genre_ratings[genre]
        avg = sum(ratings) / len(ratings)
        print(f"{genre}\t{avg:.2f}\t{len(ratings)}")


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "reduce":
        reducer()
    else:
        mapper()
