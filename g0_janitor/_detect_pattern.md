*Last updated: 2026-05-26  22:40*

# Pattern Recognition Guide — NeetCode 150

#### 1. Arrays & Hashing

*Watch out for:* using a list where a set would do · modifying a dict while iterating

| Recognize it when... | Tips |
|---|---|
| Need to check **existence or duplicates** | **Complement trick**: store `{num: index}`, look up `target - num` |
| Need to **count frequencies** | Use a **tuple** (sorted word / 26-count array) as a hashmap key for grouping |
| Find a **pair / complement** summing to target | **Set beats sort** when you only need membership — O(n) vs O(n log n) |
| **Group elements** by a shared property | Consecutive sequence: only start counting where `num - 1` is absent |
| Brute force is O(n²), need O(1) lookup | `defaultdict(list)` for grouping; `Counter` for frequencies |

#### 2. Two Pointers

*Watch out for:* forgetting to sort first · off-by-one on 1-indexed answers · infinite loop if both pointers don't advance after a match

| Recognize it when... | Tips |
|---|---|
| Array / string is **sorted** (or can be sorted) | **Move the weaker pointer** — the one limiting the answer |
| Find **pair or triplet** summing to target | **Skip duplicates** after a match: advance past repeated values |
| **Palindrome** check on a string | Sorted input + two pointers = O(n) replacement for O(n²) nested loops |
| "Container / water" area problems | For palindromes: skip non-alphanumeric inline with inner `while` |
| Brute force is O(n²) but O(n) is expected | `l` and `r` converge — they never cross, so each element visited once |

#### 3. Sliding Window

*Watch out for:* rebuilding counter each step (O(n·w) instead of O(n)) · "at most" vs "exactly" · uninitialized result for empty input

| Recognize it when... | Tips |
|---|---|
| **Longest / shortest subarray or substring** with a constraint | **Variable window**: expand `r` always, shrink `l` only when invalid |
| Condition involves **contiguous elements** only | **Fixed window**: remove `s[r - k]` before adding `s[r]` |
| "At most k distinct", "without repeating", "exactly k" | Track window state with a **Counter** — update incrementally, don't rebuild |
| Fixed-size window ("max sum of k elements") | Compute the answer **after** the shrink loop — window is always valid there |
| | "Exactly k" = `at_most(k) − at_most(k−1)` |

#### 4. Stack

*Watch out for:* popping an empty stack · wrong operand order in subtraction/division · forgetting remaining stack entries are unanswered

| Recognize it when... | Tips |
|---|---|
| **Matching / validating** brackets or nested structures | **Monotonic stack**: pop when new element breaks monotonicity — O(n) total |
| **Next greater / smaller element** for each position | Map closing bracket → expected open bracket for clean validation |
| **Evaluate an expression** (RPN, calculator) | **RPN**: numbers → push; operator → pop two, compute, push (watch operand order) |
| Need to remember "what came before" while scanning forward | After the loop, items still on stack have answer = 0 (never found "next greater") |
| **Car fleet**, temperatures — monotonic constraint | Car fleet: sort descending by position, merge if arrival time ≤ car ahead |

#### 5. Binary Search

*Watch out for:* `l <= r` vs `l < r` · infinite loop when `mid` doesn't move · off-by-one (`r = mid - 1` not `r = mid`)

| Recognize it when... | Tips |
|---|---|
| Input is **sorted** or search space is **monotonic** | Always use `mid = l + (r - l) // 2` to avoid overflow |
| O(log n) time required or implied | **Binary search on the answer**: define `feasible(x)`, search the value range |
| "Find minimum / maximum satisfying a condition" | **Rotated array**: one half is always sorted — use that half to decide direction |
| **Koko / capacity** type — optimise a threshold | `l <= r` when returning inside loop; `l < r` when answer is `l` after loop |
| Rotated sorted array | 2D matrix: `row = mid // cols`, `col = mid % cols` |

#### 6. Linked List

*Watch out for:* losing `next` before redirecting — always `nxt = curr.next` first · missing `None` checks before `.next` · forgetting `cur = cur.next` in two-pass patterns

| Recognize it when... | Tips |
|---|---|
| Structure is explicitly a linked list | **Dummy head**: use when the head itself might be removed → return `dummy.next` |
| "Reverse", "merge", "cycle", "reorder", "remove nth" | **Slow / fast pointers**: cycle detection · midpoint · kth from end |
| Need **midpoint** or **kth from end** | **Reverse**: `prev, curr = None, head` → save `nxt`, redirect, advance |
| | **Reorder**: find mid → reverse second half → interleave |
| | Two passes are often cleaner than one |

#### 7. Trees

*Watch out for:* missing base case `if not node: return` · confusing depth vs height · BST LCA: first node where `p.val ≤ node.val ≤ q.val` — no full traversal needed

| Recognize it when... | Tips |
|---|---|
| "Depth", "diameter", "path sum", "invert", "balance" | **DFS recursive** for most tree problems — values bubble up naturally |
| "Level order", "right side view", "min depth" | **BFS with deque** for anything level-by-level |
| Comparing two trees, finding subtrees | **Return multiple values** from DFS instead of using globals: `[is_balanced, height]` |
| BST: "kth smallest", "validate", "LCA" | **BST property**: left < root < right — prune half the tree on each step |
| | **Diameter**: at each node `candidate = left_height + right_height` |

#### 8. Heap / Priority Queue

*Watch out for:* forgetting to negate for max-heap · tuple tie-breaker needed if first elements can be equal · `heappop` returns smallest, not largest

| Recognize it when... | Tips |
|---|---|
| "**K largest / smallest**" elements | Python only has **min-heap** — negate values to simulate max-heap |
| "**Top K frequent**" | **Keep size at k**: push then pop if `len > k` → `heap[0]` = kth largest |
| "**Median from a stream**" | **Median**: max-heap (lower half) + min-heap (upper half), balance sizes ±1 |
| Repeatedly extract min or max efficiently | **K closest points**: max-heap of size k on negative squared distance |
| Merge K sorted lists | Heap of tuples `(priority, item)` — comparison falls through to second element |

#### 9. Backtracking

*Watch out for:* not undoing the choice after recursion · confusing "same level" duplicates (skip) vs "same path" (allowed) · grid bounds check before accessing `grid[r][c]`

| Recognize it when... | Tips |
|---|---|
| "**All** combinations / permutations / subsets" | Template: **add → recurse → remove** (always undo the choice) |
| "**Generate all valid** ..." (parentheses, N-Queens) | **Prune early**: check constraints before recursing, not after |
| Word search on a grid | **Avoid duplicates**: sort input, skip `candidates[i] == candidates[i-1]` at same tree level |
| Brute-force explores a decision tree | **Subsets**: pass a `start` index · **Permutations**: use `used[]` boolean array |
| | Grid DFS: add to `path` set before recursing, remove after |

#### 10. Tries

*Watch out for:* `is_end` checked at last node, not just when the node exists · deletion: unset `is_end`, remove nodes only if they have no other children

| Recognize it when... | Tips |
|---|---|
| **Prefix matching**, autocomplete, "starts with" | TrieNode: `children = {}` + `is_end = False` |
| Dictionary + search with **wildcards** (`.`) | **Insert**: walk chars, create nodes, set `is_end` at last char |
| Multiple strings sharing prefixes | **Wildcard `.`**: recurse into all children at that depth |
| Word Search II — find all words in a grid | **Word Search II**: build trie from word list, then DFS the grid — prune branches not in trie |

#### 11. Graphs

*Watch out for:* not marking visited before adding to BFS queue (duplicates) · cycle detection needs 3 states, not 2 · always check grid bounds before accessing `grid[r][c]`

| Recognize it when... | Tips |
|---|---|
| **Grid** problems ("islands", "area", "rotting oranges") | Grid = graph: each cell is a node, 4 directional neighbors are edges |
| Explicit adjacency list or matrix | **BFS** → shortest path / minimum steps |
| "Number of connected components" | **DFS** → connected components, flood fill |
| "Can you reach from A to B", cycle detection | **Topological sort** (DFS with 3 states: unvisited / visiting / visited) for course schedule |
| Clone a graph | **Union-Find** for connected components and redundant connections |

#### 12. Advanced Graphs

*Watch out for:* Dijkstra fails with negative weights · Kruskal's requires sorted edges · K-stop: copy prev distances before each round

| Recognize it when... | Tips |
|---|---|
| **Weighted edges** + shortest path | **Dijkstra**: min-heap of `(cost, node)` — only non-negative weights |
| **Negative weights** | **Bellman-Ford**: relax all edges V−1 times |
| **Minimum spanning tree** | **Kruskal's**: sort edges by weight + Union-Find · **Prim's**: min-heap from one node |
| "Cheapest flights within K stops" | K-stop Bellman-Ford: exactly K+1 rounds on a **copy** of distances (don't update in-place) |
| Reconstruct itinerary (Eulerian path) | DFS + post-order append → reverse result at end |

#### 13. 1-D Dynamic Programming

*Watch out for:* wrong state definition (redefine if recurrence is messy) · forgetting to memoise all arguments · circular arrays → split into two linear subproblems

| Recognize it when... | Tips |
|---|---|
| "**Number of ways** to reach / form / decode" | **Define the state first**: `dp[i]` = answer for input of size i |
| "**Max / min** profit / cost / length" | **Find the recurrence** before coding: how does `dp[i]` depend on earlier? |
| Each step has a **binary choice** (take/skip, buy/sell) | **Base cases first** — don't derive them from the recurrence |
| Recursive solution recomputes the same calls | If `dp[i]` depends only on last 1–2 values → **rolling variables**, O(1) space |
| "Contiguous subarray" (Kadane's, max product) | Top-down = easier to see; bottom-up = no recursion overhead |

#### 14. 2-D Dynamic Programming

*Watch out for:* table size `(m+1) × (n+1)` for empty-string base case · confusing "skip from text1" vs "skip from text2" in LCS / edit distance

| Recognize it when... | Tips |
|---|---|
| **Two sequences** as input (LCS, edit distance) | **State**: `dp[i][j]` = answer for `text1[:i]` and `text2[:j]` |
| Grid traversal with constraints (unique paths) | Fill order depends on dependencies — draw the table to confirm |
| State depends on **two indices** | **Reduce to 1D**: if row only depends on next row → rolling array, O(n) space |
| "Minimum operations / number of ways" between two strings | Add a third dimension for extra state (e.g. buying vs selling, cooldown) |
| | Draw and manually fill a small DP table before coding |

#### 15. Greedy

*Watch out for:* greedy doesn't always work — verify with a small counter-example · sorting direction matters (end time vs start time) · gas station: reset running sum, track start index

| Recognize it when... | Tips |
|---|---|
| "**Can you reach the end?**" / "**minimum jumps**" | **Jump Game**: track `max_reachable` — if index > max, return False |
| **Interval scheduling** — maximise non-overlapping | **Non-overlapping intervals**: sort by **end time**, keep earliest ending |
| **Partitioning** with character constraints | **Partition labels**: last occurrence of each char determines partition boundary |
| Locally optimal choice leads to global optimum | **Gas station**: if total gas ≥ total cost, solution exists; start after last deficit |
| Sorting + single scan gives the answer | Ask: "if I make a suboptimal choice now, can I recover?" — if No, greedy works |

#### 16. Intervals

*Watch out for:* not sorting before processing · merge needs `max` of both ends (not just new interval's end) · non-overlapping: sort by end time, not start

| Recognize it when... | Tips |
|---|---|
| Input is a list of **[start, end]** pairs | **Sort by start time** first — almost always the right first step |
| "**Merge overlapping intervals**" | **Overlap test**: `A.end >= B.start` (after sorting by start) |
| **Insert an interval** into a sorted list | **Merge**: `result[-1][1] = max(result[-1][1], cur[1])` |
| **Meeting rooms** — how many rooms needed | **Meeting rooms II**: min-heap of end times — reuse room if earliest end < next start |
| "Minimum intervals to cover a query" | Insert: handle three zones — fully before, overlapping, fully after |

#### 17. Math & Geometry

*Watch out for:* in-place rotation: transpose first, then reverse (naïve overwrites values) · negative exponent: `x^(-n) = 1 / x^n` · multiply strings: carry at the end of each column

| Recognize it when... | Tips |
|---|---|
| **Matrix rotation / spiral / zeroing** in-place | **Rotate 90° CW**: transpose (`swap [i][j] ↔ [j][i]`), then reverse each row |
| **Number theory**: happy number, GCD, power | **Spiral**: shrink four boundaries (top/bottom/left/right) after each direction |
| Simulating arithmetic without built-in operators | **Set zeroes**: record rows/cols in first pass, zero in second — never zero during scan |
| Power computation with large exponents | **Happy number**: set of seen values — if revisited, it's a cycle |
| | **Fast power**: `x^n = (x^(n//2))^2` → O(log n) |

#### 18. Bit Manipulation

*Watch out for:* Python integers are arbitrary precision — use `n & 0xFFFFFFFF` for 32-bit problems · `~n` in Python = `-(n+1)` · `n & (-n)` isolates the lowest set bit

| Recognize it when... | Tips |
|---|---|
| "**Single number**" where all others appear twice | `a ^ a = 0`, `a ^ 0 = a` — XOR all elements, pairs cancel |
| "**Count set bits**" / number of 1s | `n & (n - 1)` clears the lowest set bit — loop until 0, count iterations |
| "**Without using + or −**" | **Sum without +**: XOR = sum bits, `(a & b) << 1` = carry — repeat until carry = 0 |
| Powers of 2 check | **Power of 2**: `n > 0 and (n & (n - 1)) == 0` |
| Generating all subsets | **Bitmask subsets**: `mask` from `0` to `2^n − 1`; bit `i` set = element `i` included |

---

## Quick Clue → Pattern

| Clue in the problem | Pattern |
|---|---|
| Sorted array + find pair / triplet | Two Pointers |
| Longest / shortest subarray with constraint | Sliding Window |
| Unsorted, need O(1) lookup or grouping | Arrays & Hashing |
| Matching brackets, next greater element | Stack |
| Sorted, O(log n) required | Binary Search |
| Minimise / maximise over a monotonic condition | Binary Search on Answer |
| Linked list: cycle, midpoint, kth from end | Linked List (slow/fast) |
| Tree: depth, diameter, balance, path sum | Trees (DFS) |
| Tree: level order, minimum depth | Trees (BFS) |
| K largest / smallest / frequent | Heap |
| All combinations / permutations / subsets | Backtracking |
| Prefix matching, wildcard search | Trie |
| Grid flood fill, connected components | Graphs (BFS / DFS) |
| Directed graph, cycle, ordering | Graphs (Topological Sort) |
| Weighted shortest path | Advanced Graphs (Dijkstra) |
| Number of ways, overlapping subproblems | 1-D / 2-D DP |
| Two sequences, edit / match | 2-D DP |
| Locally optimal → globally optimal | Greedy |
| [start, end] pairs, merge / schedule | Intervals |
| Matrix rotate / spiral / zero | Math & Geometry |
| XOR, set bits, no arithmetic ops | Bit Manipulation |

---

## Extra Files by Category

*Auto-generated — all files beyond NeetCode 150*

**Root**
- `0.Practice.py`
- `0.input.py`
- `1.Practice.py`

**g0_oops**
- `oop1_robot.py`
- `oop2_bank_system.py`
- `oop3_shapes.py`
- `oop4_data_pipeline.py`

**g11_graphs**
- `q0_helper.py`
- `qe_compilation_order.py`
- `qe_island_perimeter.py`
- `qe_paths_in_a_maze.py`
- `qk_1_find_rectangles_in_matrix.py`

**g13_1_D_dynamic_programming**
- `qe_nth_tribonacci_number.py`
- `qe_word_break_2.py`

**g14_2_D_dynamic_programming**
- `qe_knapsack.py`

**g15_greedy-not_solved**
- `qe_boats_to_save_people.py`
- `qe_minimum_refueling_stops.py`
- `qk_1_word_wrap.py`
- `qk_2_text_justification.py`

**g16_intervals-not_solved**
- `qe_car_pooling.py`
- `qe_count_days_without_meetings.py`
- `qe_employee_free_time.py`

**g17_math_and_geometry-not_solved**
- `qe_minimum_time_taken_to_reach_destination.py`
- `qe_spiral_matrix_2.py`
- `qe_where_will_the_ball_fall.py`

**g1_arrays_and_hashing**
- `qe_cyclic_sort.py`
- `qe_first_missing_positive.py`
- `qk_1_subdomain_visit_count.py`
- `qk_2_student_course_overlap.py`
- `qk_3_access_control_mismatch.py`
- `qk_4_words_formed_by_characters.py`
- `qk_5_find_error_action.py`
- `qk_6_top_words_by_length.py`
- `qk_7_matrix_all_numbers_valid.py`

**g2_two_pointers**
- `qe_minimum_number_of_moves_to_make_palindrome.py`
- `qe_next_palindrome_using_same_digits.py`
- `qe_reverse_words_in_a_string.py`
- `qe_sort_colors.py`
- `qe_strobogrammatic_number.py`
- `qe_valid_word_abbreviation.py`

**g3_sliding_window**
- `qe_count_subarrays_with_scores_less_than_k.py`
- `qe_count_substrings_with_k_frequency_characters.py`
- `qe_diet_plan_performance.py`
- `qe_fruits_into_basket.py`
- `qe_repeated_DNA_sequences.py`
- `qe_subarrays_with_k_different_intergers.py`
- `qk_1_longest_common_subarray.py`
- `qk_2_badge_swiped_within_hour.py`
- `qk_3_hit_counter.py`

**g4_stack**
- `qe_basic_calculator.py`
- `qe_minimum_remove_to_make_valid_parantheses.py`
- `qe_number_of_vissible_people_in_a_queue.py`
- `qe_remove_all_adjacent_duplicates_in_a_string.py`

**g5_binary_search**
- `qe_divide_chocolate.py`
- `qe_find_k_closest_elements.py`
- `qe_first_bad_version.py`
- `qe_maximum_running_times_of_n_computers.py`
- `qe_maximum_value_at_a_given_index_in_a_bounded_array.py`
- `qe_minimize_max_distance_to_gas_station.py`
- `qe_search_in_rotated_sorted_array_2.py`
- `qe_split_array_larges_sum.py`

**g6_linked_list**
- `q0_helpers.py`
- `qe_circular_array_loop.py`
- `qe_palindrome_linked_list.py`

**g7_trees**
- `q0_helpers.py`
- `qe_binary_tree_cameras.py`
- `qe_flatten_tree_to_a_linkedlist.py`

**g8_heap_and_priority_queues**
- `qe_IPO.py`
- `qe_find_right_interval.py`
- `qe_maximum_performance_of_a_team.py`
- `qe_maximum_product_after_k_increments.py`
- `qe_min_cost_to_hire_k_workders.py`
- `qe_reorganize_string.py`
- `qe_schedule_tasks_on_minimum_machines.py`
- `qe_the_number_of_the_smallest_unoccupied_chair.py`

**g9_backtracking**
- `qe_combinations.py`
- `qe_letter_case_permutation.py`
- `qk_1_flood_fill.py`
- `qx1_restore_ip_addresses.py`
- `qx3_minimum_moves_to_spread_stones_over_grid.py`
- `qx4_course_paths.py`

---
