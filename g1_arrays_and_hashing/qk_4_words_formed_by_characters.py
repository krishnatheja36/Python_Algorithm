"""
Words Formed by Characters — Karat / LeetCode 1160 | Arrays & Hashing

Pattern: Counter comparison
  A word can be formed if, for every character in the word, the character
  appears at least as many times in `chars` as it does in the word.
  Use Counter to check frequencies. Sum lengths of all valid words.

Time:  O(n * m) — n words, m = average word length
Space: O(1)     — Counter bounded by alphabet size (26)
"""
from collections import Counter


def count_chars(words, chars):
    chars_count = Counter(chars)
    total = 0
    for word in words:
        word_count = Counter(word)
        if all(chars_count[c] >= word_count[c] for c in word_count):
            total += len(word)
    return total


if __name__ == "__main__":
    words = ["cat", "bt", "hat", "tree"]
    chars = "atach"
    print(count_chars(words, chars))   # 6  ("cat" + "hat")
