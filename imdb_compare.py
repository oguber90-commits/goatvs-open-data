"""Compare the GOATvs head-to-head movie ranking with IMDb ratings.

IMDb's ratings are not part of this repository. The script downloads IMDb's own daily file
(https://datasets.imdbws.com/title.ratings.tsv.gz, for personal and non-commercial use, see
https://developer.imdb.com/non-commercial-datasets/) and joins it to data/movies_items.csv on the IMDb id.

    python3 imdb_compare.py                 download the ratings file next to the script (about 8 MB), then compare
    python3 imdb_compare.py ratings.tsv.gz  use a file you already have

Only the standard library is needed.
"""
import csv
import gzip
import os
import sys
import urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
URL = "https://datasets.imdbws.com/title.ratings.tsv.gz"
WELL = 300  # a film needs this many decided duels before its raw win rate is quoted


def ratings(path):
    out = {}
    with gzip.open(path, "rt", encoding="utf-8") as f:
        next(f)
        for line in f:
            t, r, n = line.rstrip("\n").split("\t")
            out[t] = (float(r), int(n))
    return out


def spearman(xs, ys):
    n = len(xs)
    mx, my = sum(xs) / n, sum(ys) / n
    num = sum((x - mx) * (y - my) for x, y in zip(xs, ys))
    den = (sum((x - mx) ** 2 for x in xs) * sum((y - my) ** 2 for y in ys)) ** 0.5
    return num / den


def median(v):
    v = sorted(v)
    return v[len(v) // 2]


def main():
    path = sys.argv[1] if len(sys.argv) > 1 else os.path.join(HERE, "title.ratings.tsv.gz")
    if not os.path.exists(path):
        print("downloading", URL)
        urllib.request.urlretrieve(URL, path)
    rat = ratings(path)
    items = []
    for i in csv.DictReader(open(os.path.join(HERE, "data", "movies_items.csv"), encoding="utf-8")):
        if i["id"] not in rat:
            continue
        i["g"] = int(i["goatvs_rank"])
        i["r"], i["n"] = rat[i["id"]]
        i["d"] = int(i["duels"])
        i["w"] = float(i["win_rate"]) if i["win_rate"] else None
        i["year"] = int(i["year_and_genres"][:4])
        i["genre"] = i["year_and_genres"].split(" · ")[1].split(" / ")[0] if " · " in i["year_and_genres"] else ""
        items.append(i)
    # IMDb's order inside this list: rating, ties by the number of IMDb votes
    for k, i in enumerate(sorted(items, key=lambda i: (-i["r"], -i["n"]))):
        i["m"] = k + 1
    # GOATvs places counted among the films that have an IMDb rating
    for k, i in enumerate(sorted(items, key=lambda i: i["g"])):
        i["gg"] = k + 1
    print("%d films with an IMDb rating" % len(items))
    print("Spearman rank correlation, GOATvs rank vs IMDb order: %.2f" % spearman([i["gg"] for i in items], [i["m"] for i in items]))
    for top in (10, 100, 250):
        both = sum(1 for i in items if i["gg"] <= top and i["m"] <= top)
        print("in both top %d lists: %d" % (top, both))

    def row(i):
        return "  GOATvs #%-4d IMDb #%-4d %.1f  wins %s of %4d duels  %s" % (
            i["g"], i["m"], i["r"], ("%3.0f%%" % (100 * i["w"])) if i["w"] is not None else "  - ", i["d"], i["title"])

    print("\nGOATvs top 15")
    for i in sorted(items, key=lambda i: i["g"])[:15]:
        print(row(i))
    print("\nIMDb's top 25 in this list, by GOATvs place")
    for i in sorted(items, key=lambda i: i["m"])[:25]:
        print(row(i))
    well = [i for i in items if i["d"] >= WELL]
    print("\nRated 8.0+ on IMDb, picked least often (%d+ duels)" % WELL)
    for i in sorted([i for i in well if i["r"] >= 8.0], key=lambda i: i["w"])[:20]:
        print(row(i))
    print("\nRated under 8.0 on IMDb, picked most often (%d+ duels)" % WELL)
    for i in sorted([i for i in well if i["r"] < 8.0], key=lambda i: -i["w"])[:20]:
        print(row(i))
    print("\nGOATvs top 100 with the lowest IMDb ratings")
    for i in sorted([i for i in items if i["g"] <= 100], key=lambda i: i["r"])[:12]:
        print(row(i))
    print("\nBy decade: films, median of (IMDb place - GOATvs place); above zero = picked more than rated")
    by = {}
    for i in items:
        by.setdefault(i["year"] // 10 * 10 if i["year"] >= 1950 else 1940, []).append(i["m"] - i["gg"])
    for d in sorted(by):
        print("  %s %4d films  %+5d" % ("pre-1950" if d == 1940 else "%ds   " % d, len(by[d]), median(by[d])))
    print("\nBy first genre (15+ films)")
    by = {}
    for i in items:
        by.setdefault(i["genre"], []).append(i["m"] - i["gg"])
    for g in sorted(by, key=lambda g: median(by[g])):
        if len(by[g]) >= 15:
            print("  %-12s %4d films  %+5d" % (g, len(by[g]), median(by[g])))


if __name__ == "__main__":
    main()
