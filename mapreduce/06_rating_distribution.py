#!/usr/bin/env python
"""
MapReduce Job 6: Rating Distribution (count of each rating value)
Mapper: Emits (rating, 1)
Reducer: Counts occurrences of each rating value
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
            try:
                rating = float(parts[2])
                print(f"{rating}\t1")
            except ValueError:
                continue

# ---------- REDUCER ----------
def reducer():
    rating_count = defaultdict(int)

    for line in sys.stdin:
        line = line.strip()
        parts = line.split("\t")
        if len(parts) != 2:
            continue
        try:
            rating = float(parts[0])
            count = int(parts[1])
            rating_count[rating] += count
        except ValueError:
            continue

    total = sum(rating_count.values())
    for rating in sorted(rating_count.keys()):
        count = rating_count[rating]
        pct = (count / total) * 100
        print(f"{rating}\t{count}\t{pct:.2f}%")


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "reduce":
        reducer()
    else:
        mapper()
