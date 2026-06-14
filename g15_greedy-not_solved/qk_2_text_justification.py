"""
Text Justification — Karat / LeetCode 68 | Greedy

Pattern: Greedy + String
  Greedily pack words onto each line (same as word wrap).
  For full lines with multiple words: distribute spaces evenly using divmod —
  extra spaces go to the leftmost gaps first.
  For single-word lines and the final line: left-justify, pad with trailing spaces.

Time:  O(n * w) — n words, w = maxWidth
Space: O(n)     — output lines
"""


def full_justify(words, max_width):
    lines = []
    cur_line = []
    cur_word_width = 0

    for word in words:
        if len(word) + len(cur_line) + cur_word_width <= max_width:
            cur_line.append(word)
            cur_word_width += len(word)
        else:
            if len(cur_line) == 1:
                line = cur_line[0] + " " * (max_width - cur_word_width)
            else:
                space, extra = divmod(max_width - cur_word_width, len(cur_line) - 1)
                for i in range(extra):
                    cur_line[i] += " "
                line = (" " * space).join(cur_line)
            lines.append(line)
            cur_line = [word]
            cur_word_width = len(word)

    last = " ".join(cur_line)
    lines.append(last + " " * (max_width - len(last)))
    return lines


if __name__ == "__main__":
    words = ["This","is","an","example","of","text","justification."]
    for line in full_justify(words, 16):
        print(f"|{line}|")
    # |This    is    an|
    # |example  of text|
    # |justification.  |
