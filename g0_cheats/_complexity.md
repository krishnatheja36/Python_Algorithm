# Time & Space Complexity
*Last updated: 2026-05-26*

---

## Big-O Notation

| Complexity | Name         | Example                        |
|------------|--------------|--------------------------------|
| O(1)       | Constant     | Array access, hash lookup      |
| O(log n)   | Logarithmic  | Binary search                  |
| O(n)       | Linear       | Linear search, traversal       |
| O(n log n) | Linearithmic | Merge sort, heap sort          |
| O(n²)      | Quadratic    | Nested loops, bubble sort      |
| O(n³)      | Cubic        | Triple nested loops            |
| O(2ⁿ)      | Exponential  | Recursive subsets, Fibonacci   |
| O(n!)      | Factorial    | Permutations                   |

---

## Data Structure Operations

| Structure          | Access   | Search   | Insert   | Delete   | Notes                  |
|--------------------|----------|----------|----------|----------|------------------------|
| Array              | O(1)     | O(n)     | O(n)     | O(n)     |                        |
| Linked List        | O(n)     | O(n)     | O(1)     | O(1)     | With pointer to node   |
| Stack              | O(n)     | O(n)     | O(1)     | O(1)     | Top only               |
| Queue / Deque      | O(n)     | O(n)     | O(1)     | O(1)     | Front/back only        |
| Hash Table         | O(1)     | O(1)     | O(1)     | O(1)     | Avg; O(n) worst case   |
| Binary Search Tree | O(log n) | O(log n) | O(log n) | O(log n) | Balanced; O(n) worst   |
| Heap               | O(1)     | O(n)     | O(log n) | O(log n) | O(1) = min/max peek    |
| Trie               | —        | O(k)     | O(k)     | O(k)     | k = key length         |

---

## Sorting Algorithms

| Algorithm      | Best       | Average    | Worst      | Space    | Stable |
|----------------|------------|------------|------------|----------|--------|
| Bubble Sort    | O(n)       | O(n²)      | O(n²)      | O(1)     | Yes    |
| Selection Sort | O(n²)      | O(n²)      | O(n²)      | O(1)     | No     |
| Insertion Sort | O(n)       | O(n²)      | O(n²)      | O(1)     | Yes    |
| Merge Sort     | O(n log n) | O(n log n) | O(n log n) | O(n)     | Yes    |
| Quick Sort     | O(n log n) | O(n log n) | O(n²)      | O(log n) | No     |
| Heap Sort      | O(n log n) | O(n log n) | O(n log n) | O(1)     | No     |
| Counting Sort  | O(n + k)   | O(n + k)   | O(n + k)   | O(k)     | Yes    |
| Radix Sort     | O(nk)      | O(nk)      | O(nk)      | O(n + k) | Yes    |
| Tim Sort       | O(n)       | O(n log n) | O(n log n) | O(n)     | Yes    |

*Python `list.sort()` and `sorted()` use Tim Sort.*

---

## Common Algorithm Complexities

### Graph Algorithms

| Algorithm              | Time               | Space    | Notes                         |
|------------------------|--------------------|----------|-------------------------------|
| BFS                    | O(V + E)           | O(V)     | Shortest path (unweighted)    |
| DFS                    | O(V + E)           | O(V)     | Stack / recursion             |
| Dijkstra               | O((V + E) log V)   | O(V)     | Min-heap; no negative weights |
| Bellman-Ford           | O(V · E)           | O(V)     | Handles negative weights      |
| Topological Sort       | O(V + E)           | O(V)     | DAGs only                     |
| Union-Find             | O(α(n)) ≈ O(1)     | O(V)     | With path compression         |
| Prim's MST             | O(E log V)         | O(V)     | Min-heap                      |
| Kruskal's MST          | O(E log E)         | O(V)     | Sort edges + Union-Find       |

### Tree Algorithms

| Algorithm              | Time     | Space    |
|------------------------|----------|----------|
| DFS (recursive)        | O(n)     | O(h)     |
| BFS (level order)      | O(n)     | O(w)     |
| BST insert / search    | O(log n) | O(1)     |
| Construct from arrays  | O(n)     | O(n)     |

*h = height, w = max width*

### Dynamic Programming

| Pattern             | Time       | Space    | Example                    |
|---------------------|------------|----------|----------------------------|
| 1-D DP              | O(n)       | O(n)     | Climbing stairs, house rob |
| 1-D DP (optimised)  | O(n)       | O(1)     | Rolling variables          |
| 2-D DP              | O(m · n)   | O(m · n) | LCS, edit distance         |
| 2-D DP (optimised)  | O(m · n)   | O(n)     | Single rolling row         |
| Knapsack (0/1)      | O(n · W)   | O(W)     | W = capacity               |

### Searching & Sorting

| Algorithm         | Time       | Space    |
|-------------------|------------|----------|
| Linear search     | O(n)       | O(1)     |
| Binary search     | O(log n)   | O(1)     |
| Python sort       | O(n log n) | O(n)     |
| heapq.nlargest(k) | O(n log k) | O(k)     |

---

## Space Complexity — What Costs Memory

| Structure / Call        | Space        | Notes                              |
|-------------------------|--------------|------------------------------------|
| Recursion stack         | O(h)         | h = max depth                      |
| BFS queue               | O(w)         | w = max width at any level         |
| Memoisation dict        | O(states)    | All unique subproblems             |
| DP table (2-D)          | O(m · n)     | Reducible to O(n) with rolling row |
| Visited set (graph)     | O(V)         |                                    |
| Output list             | O(n)         | Don't forget to count this         |
| Sorting in Python       | O(n)         | Tim Sort needs auxiliary space     |
| In-place algorithm      | O(1)         | Two pointers, swaps                |
