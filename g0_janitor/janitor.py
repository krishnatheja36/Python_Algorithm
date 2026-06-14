"""
janitor.py — NeetCode 150 housekeeping script.

Run with: python janitor.py

Does four things:
  1. Any *-not_solved.py file that now has content → strips -not_solved from filename.
  2. Folders: re-evaluates -not_solved suffix based on current file state.
  3. Prints solved / unsolved summary to console.
  4. Writes progress.md in the same directory with a full progress report.
"""

import os
from datetime import datetime

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

NEETCODE_150 = [
    # (q_num, problem_name, group, lc_num)
    (1,   "Contains Duplicate",                                 "Arrays & Hashing",              217),
    (2,   "Valid Anagram",                                      "Arrays & Hashing",              242),
    (3,   "Two Sum",                                            "Arrays & Hashing",                1),
    (4,   "Group Anagrams",                                     "Arrays & Hashing",               49),
    (5,   "Top K Frequent Elements",                            "Arrays & Hashing",              347),
    (6,   "Encode and Decode Strings",                          "Arrays & Hashing",              271),
    (7,   "Product of Array Except Self",                       "Arrays & Hashing",              238),
    (8,   "Valid Sudoku",                                       "Arrays & Hashing",               36),
    (9,   "Longest Consecutive Sequence",                       "Arrays & Hashing",              128),
    (10,  "Valid Palindrome",                                   "Two Pointers",                  125),
    (11,  "Two Sum II - Input Array Is Sorted",                 "Two Pointers",                  167),
    (12,  "3Sum",                                               "Two Pointers",                   15),
    (13,  "Container With Most Water",                          "Two Pointers",                   11),
    (14,  "Trapping Rain Water",                                "Two Pointers",                   42),
    (15,  "Best Time to Buy And Sell Stock",                    "Sliding Window",                121),
    (16,  "Longest Substring Without Repeating Characters",     "Sliding Window",                  3),
    (17,  "Longest Repeating Character Replacement",            "Sliding Window",                424),
    (18,  "Permutation In String",                              "Sliding Window",                567),
    (19,  "Minimum Window Substring",                           "Sliding Window",                 76),
    (20,  "Sliding Window Maximum",                             "Sliding Window",                239),
    (21,  "Valid Parentheses",                                  "Stack",                          20),
    (22,  "Min Stack",                                          "Stack",                         155),
    (23,  "Evaluate Reverse Polish Notation",                   "Stack",                         150),
    (24,  "Daily Temperatures",                                 "Stack",                         739),
    (25,  "Car Fleet",                                          "Stack",                         853),
    (26,  "Largest Rectangle In Histogram",                     "Stack",                          84),
    (27,  "Binary Search",                                      "Binary Search",                 704),
    (28,  "Search a 2D Matrix",                                 "Binary Search",                  74),
    (29,  "Koko Eating Bananas",                                "Binary Search",                 875),
    (30,  "Find Minimum In Rotated Sorted Array",               "Binary Search",                 153),
    (31,  "Search In Rotated Sorted Array",                     "Binary Search",                  33),
    (32,  "Time Based Key Value Store",                         "Binary Search",                 981),
    (33,  "Median of Two Sorted Arrays",                        "Binary Search",                   4),
    (34,  "Reverse Linked List",                                "Linked List",                   206),
    (35,  "Merge Two Sorted Lists",                             "Linked List",                    21),
    (36,  "Linked List Cycle",                                  "Linked List",                   141),
    (37,  "Reorder List",                                       "Linked List",                   143),
    (38,  "Remove Nth Node From End of List",                   "Linked List",                    19),
    (39,  "Copy List With Random Pointer",                      "Linked List",                   138),
    (40,  "Add Two Numbers",                                    "Linked List",                     2),
    (41,  "Find The Duplicate Number",                          "Linked List",                   287),
    (42,  "LRU Cache",                                          "Linked List",                   146),
    (43,  "Merge K Sorted Lists",                               "Linked List",                    23),
    (44,  "Reverse Nodes In K Group",                           "Linked List",                    25),
    (45,  "Invert Binary Tree",                                 "Trees",                         226),
    (46,  "Maximum Depth of Binary Tree",                       "Trees",                         104),
    (47,  "Diameter of Binary Tree",                            "Trees",                         543),
    (48,  "Balanced Binary Tree",                               "Trees",                         110),
    (49,  "Same Tree",                                          "Trees",                         100),
    (50,  "Subtree of Another Tree",                            "Trees",                         572),
    (51,  "Lowest Common Ancestor of a BST",                    "Trees",                         235),
    (52,  "Binary Tree Level Order Traversal",                  "Trees",                         102),
    (53,  "Binary Tree Right Side View",                        "Trees",                         199),
    (54,  "Count Good Nodes In Binary Tree",                    "Trees",                        1448),
    (55,  "Validate Binary Search Tree",                        "Trees",                          98),
    (56,  "Kth Smallest Element In a BST",                      "Trees",                         230),
    (57,  "Construct Binary Tree From Preorder And Inorder",    "Trees",                         105),
    (58,  "Binary Tree Maximum Path Sum",                       "Trees",                         124),
    (59,  "Serialize And Deserialize Binary Tree",              "Trees",                         297),
    (60,  "Kth Largest Element In a Stream",                    "Heap / Priority Queue",         703),
    (61,  "Last Stone Weight",                                  "Heap / Priority Queue",        1046),
    (62,  "K Closest Points to Origin",                         "Heap / Priority Queue",         973),
    (63,  "Kth Largest Element In An Array",                    "Heap / Priority Queue",         215),
    (64,  "Task Scheduler",                                     "Heap / Priority Queue",         621),
    (65,  "Design Twitter",                                     "Heap / Priority Queue",         355),
    (66,  "Find Median From Data Stream",                       "Heap / Priority Queue",         295),
    (67,  "Subsets",                                            "Backtracking",                   78),
    (68,  "Combination Sum",                                    "Backtracking",                   39),
    (69,  "Combination Sum II",                                 "Backtracking",                   40),
    (70,  "Permutations",                                       "Backtracking",                   46),
    (71,  "Subsets II",                                         "Backtracking",                   90),
    (72,  "Generate Parentheses",                               "Backtracking",                   22),
    (73,  "Word Search",                                        "Backtracking",                   79),
    (74,  "Palindrome Partitioning",                            "Backtracking",                  131),
    (75,  "Letter Combinations of a Phone Number",              "Backtracking",                   17),
    (76,  "N Queens",                                           "Backtracking",                   51),
    (77,  "Implement Trie Prefix Tree",                         "Tries",                         208),
    (78,  "Design Add And Search Words Data Structure",         "Tries",                         211),
    (79,  "Word Search II",                                     "Tries",                         212),
    (80,  "Number of Islands",                                  "Graphs",                        200),
    (81,  "Max Area of Island",                                 "Graphs",                        695),
    (82,  "Clone Graph",                                        "Graphs",                        133),
    (83,  "Walls And Gates",                                    "Graphs",                        286),
    (84,  "Rotting Oranges",                                    "Graphs",                        994),
    (85,  "Pacific Atlantic Water Flow",                        "Graphs",                        417),
    (86,  "Surrounded Regions",                                 "Graphs",                        130),
    (87,  "Course Schedule",                                    "Graphs",                        207),
    (88,  "Course Schedule II",                                 "Graphs",                        210),
    (89,  "Graph Valid Tree",                                   "Graphs",                        261),
    (90,  "Number of Connected Components In Undirected Graph", "Graphs",                        323),
    (91,  "Redundant Connection",                               "Graphs",                        684),
    (92,  "Word Ladder",                                        "Graphs",                        127),
    (93,  "Network Delay Time",                                 "Advanced Graphs",               743),
    (94,  "Reconstruct Itinerary",                              "Advanced Graphs",               332),
    (95,  "Min Cost to Connect All Points",                     "Advanced Graphs",              1584),
    (96,  "Swim In Rising Water",                               "Advanced Graphs",               778),
    (97,  "Alien Dictionary",                                   "Advanced Graphs",               269),
    (98,  "Cheapest Flights Within K Stops",                    "Advanced Graphs",               787),
    (99,  "Climbing Stairs",                                    "1-D Dynamic Programming",        70),
    (100, "Min Cost Climbing Stairs",                           "1-D Dynamic Programming",       746),
    (101, "House Robber",                                       "1-D Dynamic Programming",       198),
    (102, "House Robber II",                                    "1-D Dynamic Programming",       213),
    (103, "Longest Palindromic Substring",                      "1-D Dynamic Programming",         5),
    (104, "Palindromic Substrings",                             "1-D Dynamic Programming",       647),
    (105, "Decode Ways",                                        "1-D Dynamic Programming",        91),
    (106, "Coin Change",                                        "1-D Dynamic Programming",       322),
    (107, "Maximum Product Subarray",                           "1-D Dynamic Programming",       152),
    (108, "Word Break",                                         "1-D Dynamic Programming",       139),
    (109, "Longest Increasing Subsequence",                     "1-D Dynamic Programming",       300),
    (110, "Partition Equal Subset Sum",                         "1-D Dynamic Programming",       416),
    (111, "Unique Paths",                                       "2-D Dynamic Programming",        62),
    (112, "Longest Common Subsequence",                         "2-D Dynamic Programming",      1143),
    (113, "Best Time to Buy And Sell Stock With Cooldown",      "2-D Dynamic Programming",       309),
    (114, "Coin Change II",                                     "2-D Dynamic Programming",       518),
    (115, "Target Sum",                                         "2-D Dynamic Programming",       494),
    (116, "Interleaving String",                                "2-D Dynamic Programming",        97),
    (117, "Longest Increasing Path In a Matrix",                "2-D Dynamic Programming",       329),
    (118, "Distinct Subsequences",                              "2-D Dynamic Programming",       115),
    (119, "Edit Distance",                                      "2-D Dynamic Programming",        72),
    (120, "Burst Balloons",                                     "2-D Dynamic Programming",       312),
    (121, "Regular Expression Matching",                        "2-D Dynamic Programming",        10),
    (122, "Maximum Subarray",                                   "Greedy",                         53),
    (123, "Jump Game",                                          "Greedy",                         55),
    (124, "Jump Game II",                                       "Greedy",                         45),
    (125, "Gas Station",                                        "Greedy",                        134),
    (126, "Hand of Straights",                                  "Greedy",                        846),
    (127, "Merge Triplets to Form Target Triplet",              "Greedy",                       1899),
    (128, "Partition Labels",                                   "Greedy",                        763),
    (129, "Valid Parenthesis String",                           "Greedy",                        678),
    (130, "Insert Interval",                                    "Intervals",                      57),
    (131, "Merge Intervals",                                    "Intervals",                      56),
    (132, "Non Overlapping Intervals",                          "Intervals",                     435),
    (133, "Meeting Rooms",                                      "Intervals",                     252),
    (134, "Meeting Rooms II",                                   "Intervals",                     253),
    (135, "Minimum Interval to Include Each Query",             "Intervals",                    2276),
    (136, "Rotate Image",                                       "Math & Geometry",                48),
    (137, "Spiral Matrix",                                      "Math & Geometry",                54),
    (138, "Set Matrix Zeroes",                                  "Math & Geometry",                73),
    (139, "Happy Number",                                       "Math & Geometry",               202),
    (140, "Plus One",                                           "Math & Geometry",                66),
    (141, "Pow(x, n)",                                          "Math & Geometry",                50),
    (142, "Multiply Strings",                                   "Math & Geometry",                43),
    (143, "Detect Squares",                                     "Math & Geometry",              2013),
    (144, "Single Number",                                      "Bit Manipulation",              136),
    (145, "Number of 1 Bits",                                   "Bit Manipulation",              191),
    (146, "Counting Bits",                                      "Bit Manipulation",              338),
    (147, "Reverse Bits",                                       "Bit Manipulation",              190),
    (148, "Missing Number",                                     "Bit Manipulation",              268),
    (149, "Sum of Two Integers",                                "Bit Manipulation",              371),
    (150, "Reverse Integer",                                    "Bit Manipulation",                7),
]


def find_q_file(q_num):
    """Search all group folders for q{num}_*.py. Returns (path, is_not_solved)."""
    prefix = f"q{q_num}_"
    for entry in os.listdir(BASE):
        folder = os.path.join(BASE, entry)
        if not os.path.isdir(folder) or not entry.startswith("g"):
            continue
        for f in os.listdir(folder):
            if f.startswith(prefix) and f.endswith(".py"):
                return os.path.join(folder, f), "-not_solved" in f
    return None, False


def has_solution(path):
    """Return True if the file contains code beyond a module-level docstring."""
    try:
        with open(path) as f:
            content = f.read()
    except Exception:
        return False
    stripped = content.strip()
    if not stripped:
        return False
    # Skip past a leading triple-quoted docstring, then check for remaining code
    if stripped.startswith('"""') or stripped.startswith("'''"):
        quote = stripped[:3]
        end = stripped.find(quote, 3)
        if end == -1:
            return False
        after = stripped[end + 3:].strip()
        return bool(after)
    return True


def step1_fix_files():
    """Strip -not_solved from any file that now has content."""
    renamed = []
    for entry in os.listdir(BASE):
        folder = os.path.join(BASE, entry)
        if not os.path.isdir(folder) or not entry.startswith("g"):
            continue
        for f in os.listdir(folder):
            # only touch NC150 files: q followed by a digit (q1_, q27_, q150_, etc.)
            if not (f.startswith("q") and len(f) > 1 and f[1].isdigit()):
                continue
            if "-not_solved" in f and f.endswith(".py"):
                full = os.path.join(folder, f)
                if has_solution(full):
                    new_name = f.replace("-not_solved", "")
                    os.rename(full, os.path.join(folder, new_name))
                    renamed.append(f"  {f}  →  {new_name}")

    if renamed:
        print("Files unmarked as not_solved:")
        for r in renamed:
            print(r)
    else:
        print("No newly solved files detected.")


def step2_fix_folders():
    """Add or remove -not_solved on folders based on current file state."""
    renamed = []
    for entry in os.listdir(BASE):
        folder = os.path.join(BASE, entry)
        if not os.path.isdir(folder) or not entry.startswith("g"):
            continue

        q_files = [
            f for f in os.listdir(folder)
            if f.startswith("q") and f[1].isdigit() and not f.startswith("q0") and f.endswith(".py")
        ]
        if not q_files:
            continue

        all_unsolved = all("-not_solved" in f for f in q_files)
        is_unsolved_folder = entry.endswith("-not_solved")

        if all_unsolved and not is_unsolved_folder:
            new_path = folder + "-not_solved"
            os.rename(folder, new_path)
            renamed.append(f"  {entry}  →  {entry}-not_solved")
        elif not all_unsolved and is_unsolved_folder:
            new_name = entry.replace("-not_solved", "")
            os.rename(folder, os.path.join(BASE, new_name))
            renamed.append(f"  {entry}  →  {new_name}")

    if renamed:
        print("\nFolders updated:")
        for r in renamed:
            print(r)


def build_results():
    """Collect solved/unsolved status for all 150 problems."""
    results = []
    for q_num, name, group, lc_num in NEETCODE_150:
        path, is_not_solved = find_q_file(q_num)
        solved = path is not None and not is_not_solved and has_solution(path)
        results.append((group, q_num, name, lc_num, solved))
    return results


def print_status(results):
    """Print solved / unsolved for all 150 problems to console."""
    solved_count = sum(1 for _, _, _, _, solved in results if solved)
    current_group = None

    print("\n" + "=" * 62)
    print("  NeetCode 150 — Progress")
    print("=" * 62)

    for group, q_num, name, lc_num, solved in results:
        if group != current_group:
            current_group = group
            print(f"\n  {group}")
            print(f"  {'─' * len(group)}")
        status = "✓" if solved else "✗"
        print(f"    {status}  q{q_num:<3}  LC{lc_num:<5}  {name}")

    remaining = 150 - solved_count
    pct = solved_count * 100 // 150
    print("\n" + "=" * 62)
    print(f"  Solved:    {solved_count} / 150  ({pct}%)")
    print(f"  Remaining: {remaining}")
    print("=" * 62)


def _progress_bar(solved, total, width=32):
    filled = int(width * solved / total)
    bar = "█" * filled + "░" * (width - filled)
    return f"`[{bar}]  {solved * 100 // total}%`"


def write_progress_md(results):
    """Write a full progress report to g0_janitor/progress.md."""
    solved_count = sum(1 for _, _, _, _, s in results if s)
    remaining = 150 - solved_count
    pct = solved_count * 100 // 150
    timestamp = datetime.now().strftime("%Y-%m-%d  %H:%M")

    # --- per-category stats ---
    cat_stats = {}
    for group, _, _, _, solved in results:
        if group not in cat_stats:
            cat_stats[group] = [0, 0]
        cat_stats[group][1] += 1
        if solved:
            cat_stats[group][0] += 1

    lines = []

    # Header
    lines += [
        "# NeetCode 150 — Progress",
        f"*Last updated: {timestamp}*",
        "",
        "---",
        "",
        "## Summary",
        "",
        f"**{solved_count} / 150 solved ({pct}%)**  ·  {remaining} remaining",
        "",
        _progress_bar(solved_count, 150),
        "",
        "---",
        "",
        "## By Category",
        "",
        "| Category | Solved | Total | % |",
        "|---|:---:|:---:|:---:|",
    ]

    for group, (s, t) in cat_stats.items():
        cat_pct = f"{s * 100 // t}%" if t else "—"
        lines.append(f"| {group} | {s} | {t} | {cat_pct} |")

    lines += ["", "---", "", "## Full Problem List", ""]

    current_group = None
    for group, q_num, name, lc_num, solved in results:
        if group != current_group:
            current_group = group
            g_solved, g_total = cat_stats[group]
            lines += [f"### {group}  ({g_solved}/{g_total})", ""]
        checkbox = "x" if solved else " "
        lines.append(f"- [{checkbox}] `q{q_num}` `LC{lc_num}` &nbsp; {name}")

    lines += ["", "---", f"*Generated by janitor.py*"]

    out_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "_progress.md")
    with open(out_path, "w") as f:
        f.write("\n".join(lines) + "\n")

    print(f"\n  Progress report written → {out_path}")




def _local_module_names():
    """Return set of module names that are local project files (to exclude)."""
    local = set()
    for root, dirs, files in os.walk(BASE):
        dirs[:] = [d for d in dirs if d != '__pycache__']
        for fname in files:
            if fname.endswith('.py'):
                local.add(fname[:-3])
    return local

# Modules used only by janitor itself — not algorithm-relevant
_JANITOR_ONLY = {'os', 'datetime'}


def extract_codebase_imports():
    """Walk all .py files in the repo, collect unique stdlib import lines grouped by module."""
    local_names = _local_module_names()
    skip = local_names | _JANITOR_ONLY
    import_map = {}

    janitor_dir = os.path.dirname(os.path.abspath(__file__))

    for root, dirs, files in os.walk(BASE):
        dirs[:] = [d for d in dirs if d != '__pycache__']
        if os.path.abspath(root) == janitor_dir:   # skip g0_janitor itself
            continue
        for fname in sorted(files):
            if not fname.endswith('.py'):
                continue
            fpath = os.path.join(root, fname)
            try:
                with open(fpath) as f:
                    for line in f:
                        line = line.strip()
                        if not (line.startswith('import ') or line.startswith('from ')):
                            continue
                        parts = line.split()
                        if line.startswith('from '):
                            # must be: from <module> import <something>
                            if len(parts) < 3 or parts[2] != 'import':
                                continue
                            module = parts[1].split('.')[0]
                        else:
                            module = parts[1].split('.')[0].split(',')[0].rstrip(';')
                        if not module.isidentifier():
                            continue
                        if module in skip:
                            continue
                        import_map.setdefault(module, set()).add(line)
            except Exception:
                pass

    return dict(sorted(import_map.items()))


def build_results():
    """Collect solved/unsolved status for all 150 problems."""
    results = []
    for q_num, name, group, lc_num in NEETCODE_150:
        path, is_not_solved = find_q_file(q_num)
        solved = path is not None and not is_not_solved and has_solution(path)
        results.append((group, q_num, name, lc_num, solved))
    return results


def print_status(results):
    """Print solved / unsolved for all 150 problems to console."""
    solved_count = sum(1 for _, _, _, _, solved in results if solved)
    current_group = None

    print("\n" + "=" * 62)
    print("  NeetCode 150 — Progress")
    print("=" * 62)

    for group, q_num, name, lc_num, solved in results:
        if group != current_group:
            current_group = group
            print(f"\n  {group}")
            print(f"  {'─' * len(group)}")
        status = "✓" if solved else "✗"
        print(f"    {status}  q{q_num:<3}  LC{lc_num:<5}  {name}")

    remaining = 150 - solved_count
    pct = solved_count * 100 // 150
    print("\n" + "=" * 62)
    print(f"  Solved:    {solved_count} / 150  ({pct}%)")
    print(f"  Remaining: {remaining}")
    print("=" * 62)


def _progress_bar(solved, total, width=32):
    filled = int(width * solved / total)
    bar = "█" * filled + "░" * (width - filled)
    return f"`[{bar}]  {solved * 100 // total}%`"


def write_progress_md(results):
    """Write a full progress report to g0_janitor/_progress.md."""
    solved_count = sum(1 for _, _, _, _, s in results if s)
    remaining = 150 - solved_count
    pct = solved_count * 100 // 150
    timestamp = datetime.now().strftime("%Y-%m-%d  %H:%M")

    cat_stats = {}
    for group, _, _, _, solved in results:
        if group not in cat_stats:
            cat_stats[group] = [0, 0]
        cat_stats[group][1] += 1
        if solved:
            cat_stats[group][0] += 1

    lines = [
        "# NeetCode 150 — Progress",
        f"*Last updated: {timestamp}*",
        "",
        "---",
        "",
        "## Summary",
        "",
        f"**{solved_count} / 150 solved ({pct}%)**  ·  {remaining} remaining",
        "",
        _progress_bar(solved_count, 150),
        "",
        "---",
        "",
        "## By Category",
        "",
        "| Category | Solved | Total | % |",
        "|---|:---:|:---:|:---:|",
    ]

    for group, (s, t) in cat_stats.items():
        cat_pct = f"{s * 100 // t}%" if t else "—"
        lines.append(f"| {group} | {s} | {t} | {cat_pct} |")

    lines += ["", "---", "", "## Full Problem List", ""]

    current_group = None
    for group, q_num, name, lc_num, solved in results:
        if group != current_group:
            current_group = group
            g_solved, g_total = cat_stats[group]
            lines += [f"### {group}  ({g_solved}/{g_total})", ""]
        checkbox = "x" if solved else " "
        lines.append(f"- [{checkbox}] `q{q_num}` `LC{lc_num}` &nbsp; {name}")

    lines += ["", "---", f"*Generated by janitor.py*"]

    out_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "_progress.md")
    with open(out_path, "w") as f:
        f.write("\n".join(lines) + "\n")

    print(f"\n  Progress report written → {out_path}")


def scan_extra_files():
    """
    Walk all group folders and collect files that are NOT NeetCode 150 q-files.
    Returns dict: folder_name -> sorted list of filenames.
    """
    janitor_dir = os.path.dirname(os.path.abspath(__file__))
    nc150_prefix = {f"q{n}_" for n in range(1, 151)}

    extra = {}
    for entry in sorted(os.listdir(BASE)):
        folder = os.path.join(BASE, entry)
        if not os.path.isdir(folder):
            continue
        if os.path.abspath(folder) == janitor_dir:
            continue
        files = []
        for fname in sorted(os.listdir(folder)):
            if not fname.endswith('.py'):
                continue
            # skip NC150 q-files (q1_ ... q150_)
            is_nc150 = any(fname.startswith(p) for p in nc150_prefix)
            if is_nc150:
                continue
            files.append(fname)
        if files:
            extra[entry] = files
    return extra


def write_detect_pattern_md(extra_files):
    """Update the auto-generated Extra Files section in g0_janitor/_detect_pattern.md."""
    import re as _re
    timestamp = datetime.now().strftime("%Y-%m-%d  %H:%M")

    # Build extra-files section
    section_lines = ["## Extra Files by Category", "", "*Auto-generated — all files beyond NeetCode 150*", ""]

    # Root-level files (no subfolder)
    root_extras = []
    for entry in sorted(os.listdir(BASE)):
        path = os.path.join(BASE, entry)
        if os.path.isfile(path) and entry.endswith('.py'):
            root_extras.append(entry)
    if root_extras:
        section_lines.append("**Root**")
        for f in root_extras:
            section_lines.append(f"- `{f}`")
        section_lines.append("")

    for folder, files in extra_files.items():
        section_lines.append(f"**{folder}**")
        for f in files:
            section_lines.append(f"- `{f}`")
        section_lines.append("")

    section_lines.append("---")
    new_section = "\n".join(section_lines)

    out_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "_detect_pattern.md")
    with open(out_path) as f:
        content = f.read()

    # Update timestamp if present, otherwise prepend one
    if _re.search(r'\*Last updated:.*?\*', content):
        content = _re.sub(r'\*Last updated:.*?\*', f'*Last updated: {timestamp}*', content)
    else:
        content = f"*Last updated: {timestamp}*\n\n" + content

    # Replace or append the Extra Files section
    if '## Extra Files by Category' in content:
        content = _re.sub(
            r'## Extra Files by Category\n.*',
            new_section,
            content,
            flags=_re.DOTALL,
        )
    else:
        content = content.rstrip() + "\n\n---\n\n" + new_section + "\n"

    with open(out_path, "w") as f:
        f.write(content)

    total = sum(len(v) for v in extra_files.values())
    print(f"  Pattern guide updated  → {out_path}  ({total} extra files indexed)")


def write_cheat_sheet():
    """Update the Imports section in g0_cheats/_cheat_sheet.md from the live codebase scan."""
    import re as _re
    import_map = extract_codebase_imports()
    timestamp = datetime.now().strftime("%Y-%m-%d  %H:%M")

    # Build new imports block
    import_lines = ["## Imports", "", "```python"]
    for module, stmts in import_map.items():
        for stmt in sorted(stmts):
            import_lines.append(stmt)
    import_lines += ["```", ""]
    new_imports_block = "\n".join(import_lines)

    cheat_path = os.path.join(BASE, "g0_cheats", "_cheat_sheet.md")
    with open(cheat_path) as f:
        content = f.read()

    # Update timestamp line
    content = _re.sub(r'\*Last updated:.*?\*', f'*Last updated: {timestamp}*', content)

    # Replace just the Imports section (between ## Imports and the next ---)
    content = _re.sub(
        r'## Imports\n.*?(?=\n---)',
        new_imports_block,
        content,
        flags=_re.DOTALL,
    )

    with open(cheat_path, "w") as f:
        f.write(content)

    print(f"  Cheat sheet updated    → {cheat_path}")


if __name__ == "__main__":
    print("=" * 62)
    print("  Janitor running...")
    print("=" * 62 + "\n")
    step1_fix_files()
    step2_fix_folders()
    results = build_results()
    print_status(results)
    write_progress_md(results)
    extra = scan_extra_files()
    write_detect_pattern_md(extra)
    write_cheat_sheet()
