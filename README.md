# GOATvs open data: what people pick when two greats go head to head

[GOATvs](https://goatvs.com/?s=r-gh-od) ranks the greatest of all time by asking one question again and again: here are two
names, which is greater? This repository holds the added-up picks of real visitors for the two lists with the most
votes, **Movies** (1,800 films) and **Songs, English & Global** (3,502 songs). The live lists: [Movies](https://goatvs.com/top/movies?s=r-gh-od) ·
[Songs](https://goatvs.com/top/songs?s=r-gh-od).

Data as of 10 November 2026, 18:20 UTC.

| List | Names | Decided picks | Skips | Pairs met | Voters |
|---|---|---|---|---|---|
| Movies | 1,800 | 169,245 | 56,262 | 154,948 | 555 |
| Songs, English & Global | 3,502 | 135,752 | 30,370 | 128,328 | 546 |

There is nothing about a single person in here: no user ids, no dates, no order of picks. Only totals.

## What we found: IMDb's ratings against head-to-head picks

A rating asks "how good is this film?". A duel asks "which of these two would you take?". They are different
questions, and the answers differ in a consistent way. (`python3 imdb_compare.py` prints everything below.)

**The same top three as IMDb, in reverse order.** IMDb's list runs The Shawshank Redemption, The Godfather, The Dark
Knight. Head to head it is The Dark Knight, The Godfather, The Shawshank Redemption:

| Duel | Picks |
|---|---|
| The Dark Knight vs The Godfather | 117 – 94 |
| The Dark Knight vs The Shawshank Redemption | 90 – 55 |
| The Godfather vs The Shawshank Redemption | 90 – 47 |

**The two orders agree, loosely.** Over the 1,799 films that have an IMDb rating, the rank correlation (Spearman) is
0.60. Six films are in both top 10s, 57 in both top 100s, 144 in both top 250s.

**Films people rate highly and then don't pick.** Among films with 300 or more duels:

| Film | IMDb rating | Wins |
|---|---|---|
| The Intouchables | 8.5 | 14% of 362 duels |
| Léon: The Professional | 8.5 | 19% of 717 |
| American Beauty | 8.3 | 21% |
| Joker | 8.3 | 27% of 1,037 |
| The Pianist | 8.5 | 32% |
| Schindler's List (IMDb #5 in this list, GOATvs #34) | 9.0 | 48% of 1,455 |
| The Green Mile (IMDb #23, GOATvs #61) | 8.6 | 39% of 1,154 |

**Films people rate modestly and then pick anyway.**

| Film | IMDb rating | Wins |
|---|---|---|
| Airplane! | 7.7 | 83% of 489 duels |
| Anchorman | 7.1 | 81% |
| The Blues Brothers | 7.9 | 81% |
| E.T. the Extra-Terrestrial | 7.9 | 76% |
| Ghostbusters | 7.8 | 74% |
| Jurassic Park (IMDb #111 in this list, GOATvs #14) | 8.2 | 70% of 1,752 |

**By genre and decade.** Take each film's place in the IMDb order and its place in the GOATvs order, and look at the
median gap per group (positive: picked more than rated).

| First genre | Films | Median gap |
|---|---|---|
| Horror | 100 | +197 |
| Action | 593 | +151 |
| Comedy | 273 | +79 |
| Adventure | 271 | −38 |
| Crime | 128 | −69 |
| Drama | 284 | −164 |
| Biography | 105 | −316 |
| Animation | 19 | −510 |

| Decade | Films | Median gap |
|---|---|---|
| before 1950 | 28 | −684 |
| 1950s | 31 | −535 |
| 1960s | 44 | −225 |
| 1970s | 60 | −65 |
| 1980s | 142 | +9 |
| 1990s | 263 | +13 |
| 2000s | 463 | +74 |
| 2010s | 521 | +60 |
| 2020s | 247 | 0 |

In short: asked for a rating, people reward the film they respect. Asked to choose, they take the one they would
watch again.

**Songs.** The head-to-head top ten: Bohemian Rhapsody, Smells Like Teen Spirit, Stairway to Heaven, Hotel
California, Billie Jean, Creep, Mr. Brightside, Smooth Criminal, Let It Be, Thriller. Bohemian Rhapsody wins 76% of
its 2,340 duels and beats Smells Like Teen Spirit 115 – 77.

## Read this before you draw conclusions

- **Few voters, and a few of them did most of the voting.** 555 people for Movies, 546 for Songs. The median voter
  made 36 picks (Movies) or 44 (Songs); the busiest tenth made about three quarters of all picks. This is a sample of
  people who like ranking things on the internet, not of the public.
- **A win rate is not the rank.** Duels are mostly between names near each other's level, so a film low in the list
  can win most of its duels against its neighbours. Sunset Boulevard wins 83% of 286 duels and sits at #602; Singin'
  in the Rain wins 75% of 479 and sits at #534. The rank (`goatvs_rank`) comes from a model that accounts for who a
  name was up against and caps each voter's weight; see "How the rank is made".
- **Most names have few duels.** The median film has 96 decided duels; 241 films have 300 or more. The median song
  has 34. The findings above lean on the well-sampled names.
- **Most pairs met once.** Of the 154,948 film pairs, 255 have 30 or more decided picks and 1,424 have 10 or more.
  Use single pairs only where they were met often; use the rest in aggregate.
- **The list decides who is compared.** The 1,800 films and 3,502 songs were chosen by how well known they are
  (IMDb votes, Wikipedia, charts and playlists), so this is not a sample of all films or all songs.
- **IMDb numbers quoted here** are from IMDb's ratings file of 27 September 2026. "IMDb #5 in this list" means fifth
  by rating among these 1,800 films, not a place in IMDb's own Top 250.

## What is counted

The same rule the site uses for its rankings:

- picks by people, in a duel on the site; votes that look automated are left out;
- a guest's picks count from their second day of voting; members' picks always count;
- a pick counts if both names are in the list today.

Two more things are left out of this dataset because it is about picks made in a duel: the site's own admin
accounts, and picks that came from an imported ratings file (members can import their IMDb, Letterboxd, Goodreads or
Spotify history; 21,344 such picks in Movies and 3,077 in Songs are not in these files).

GOATvs has other lists too. Before a list has many votes, its order still leans on where the list started (how
well known each name is), so those lists are not published here. The two lists in this repository have enough votes
that the order comes from the picks.

## How the rank is made

Each list is fitted with the Bradley-Terry model on an Elo-like scale (400 points = 10 to 1 odds). Before any votes,
each name starts from how well known it is; the fit is a MAP estimate with that starting point as the prior, so a
name with few duels stays near where it started and a name with many is placed by its results. Each voter's weight
in a list is capped (300 picks' worth), and so is the weight one voter can put on a single name (8 picks' worth), so
a few very busy voters cannot decide a list. The site shows how it works in plain words at
[goatvs.com/about](https://goatvs.com/about?s=r-gh-od).

`goatvs_rank` and `goatvs_rating` are the live list at the time of the export. The live list also counts imported
picks and admin accounts, which the win/loss columns here leave out, so refitting from the pairs file will give a
slightly different order.

## Files

`data/movies_items.csv`, `data/songs_items.csv`: one row per name.

| Column | Meaning |
|---|---|
| `id` | Movies: IMDb id (`tt…`). Songs: Wikidata id (`Q…`) or Deezer track id (`dz…`) |
| `title` | Name |
| `year_and_genres` (movies) / `artist` (songs) | Year and genres as "1994 · Crime / Drama", or the artist |
| `goatvs_rank`, `goatvs_rating` | Place and rating in the GOATvs list |
| `duels` | Decided duels (`wins` + `losses`) |
| `wins`, `losses` | Times picked, times the other name was picked |
| `win_rate` | `wins / duels` |
| `skips` | Duels with this name that the voter passed ("Don't know / skip") |

`data/movies_pairs.csv`, `data/songs_pairs.csv`: one row per pair that met at least once, most-met first.

| Column | Meaning |
|---|---|
| `a_id`, `b_id`, `a_title`, `b_title` | The two names (`a_id` sorts before `b_id`) |
| `a_wins`, `b_wins` | Times each was picked over the other |
| `skips` | Times the pair was skipped |

`data/meta.json`: the totals in the table at the top.

`imdb_compare.py`: joins the movies file to IMDb's own ratings file and prints the comparison. IMDb's ratings are
not in this repository; the script downloads IMDb's daily file (for personal and non-commercial use, see
[IMDb's terms](https://developer.imdb.com/non-commercial-datasets/)). Python 3, standard library only:

```
python3 imdb_compare.py
```

## Licence and credit

The data and the text are under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/): use them for anything,
with credit to "GOATvs (goatvs.com)". The script is under the MIT licence (see `LICENSE`).

Information courtesy of IMDb (https://www.imdb.com). Used with permission.

Questions, mistakes, ideas: hello@goatvs.com
