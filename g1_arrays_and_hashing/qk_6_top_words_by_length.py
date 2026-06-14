"""
Top Words by Length — Karat | Arrays & Hashing

Pattern: Hash Map + Sorting (same family as Top K Frequent Elements q5)
  Parse each "word,length" entry into a dict, keeping only entries whose
  length exceeds minwordLength. Sort by length descending, return top wordLimit keys.

Time:  O(n log n) — sorting dominates
Space: O(n)
"""


def get_top_words(s, word_limit, min_word_length):
    word_map = {}
    for entry in s:
        key, value = entry.split(",")
        key = key.strip()
        value = int(value.strip())
        if value > min_word_length:
            word_map[key] = value

    return sorted(word_map, key=word_map.get, reverse=True)[:word_limit]


if __name__ == "__main__":
    s = [
        "abc, 500", "sadhasjhkgdsak, 230239203", "fsgdfssd, 78",
        "sss, 56",  "ss, 56", "sss, 5678", "sssdsds, 56", "ssssdsd, 56",
    ]
    print(get_top_words(s, word_limit=4, min_word_length=3))
