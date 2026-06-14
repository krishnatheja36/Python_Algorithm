"""
Word Wrap — Karat | Greedy

Pattern: Greedy
  Greedily pack as many words as possible onto the current line without
  exceeding width n (accounting for separators between words).
  When a word no longer fits, flush the current line and start a new one.
  Join words on each line with a delimiter (here "-").

Time:  O(n) — single pass through words
Space: O(n) — output lines
"""


def word_wrap(words, n):
    lines = []
    cur_line = []
    cur_width = 0

    for word in words:
        needed = cur_width + len(word) + len(cur_line)  # len(cur_line) = separators
        if needed <= n:
            cur_line.append(word)
            cur_width += len(word)
        else:
            lines.append("-".join(cur_line))
            cur_line = [word]
            cur_width = len(word)

    lines.append("-".join(cur_line))
    return lines


if __name__ == "__main__":
    words = ["1p3acres", "is", "a", "good", "place", "to", "communicate"]
    print(word_wrap(words, 12))
    # ['1p3acres-is-a', 'good-place-to', 'communicate']
