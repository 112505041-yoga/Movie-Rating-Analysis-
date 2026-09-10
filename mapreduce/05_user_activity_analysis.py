#!/usr/bin/env python
"""
MapReduce Job 5: User Activity Analysis
Mapper: Emits (userId, rating)
Reducer: Computes total ratings, average rating per user
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
            user_id = parts[0]
            try:
                rating = float(parts[2])
                print(f"{user_id}\t{rating}")
            except ValueError:
                continue

# ---------- REDUCER ----------
def reducer():
    user_ratings = defaultdict(list)

    for line in sys.stdin:
        line = line.strip()
        parts = line.split("\t")
        if len(parts) != 2:
            continue
        user_id = parts[0]
        try:
            rating = float(parts[1])
            user_ratings[user_id].append(rating)
        except ValueError:
            continue

    # Sort by number of ratings descending
    sorted_users = sorted(user_ratings.items(), key=lambda x: -len(x[1]))

    print("userId\ttotalRatings\tavgRating\tminRating\tmaxRating")
    for user_id, ratings in sorted_users[:30]:
        avg = sum(ratings) / len(ratings)
        print(f"{user_id}\t{len(ratings)}\t{avg:.2f}\t{min(ratings)}\t{max(ratings)}")


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "reduce":
        reducer()
    else:
        mapper()
