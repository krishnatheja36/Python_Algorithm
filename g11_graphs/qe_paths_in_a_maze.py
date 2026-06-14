"""
Paths in a Maze (Number of Triangles) — Graphs

Logic:
    Build an undirected graph from corridor pairs. For each new corridor (room1,
    room2), count how many existing neighbours the two rooms share — each shared
    neighbour forms a triangle (3-cycle). The shared neighbour count is the
    intersection size of both neighbour sets.

Time:  O(E * V) — for each new edge, the neighbour intersection can be O(V)
Space: O(V + E) — adjacency sets for all nodes
"""

from collections import defaultdict

class Solution:

    def number_of_paths(self, n, corridors):
        neighbours = defaultdict(set)
        cycles = 0

        for room1, room2 in corridors:
            neighbours[room1].add(room2)
            neighbours[room2].add(room1)
            cycles += len(neighbours[room1].intersection(neighbours[room2]))
            
        return cycles


if __name__ == '__main__':
    S = Solution()
    n_list = [5, 4, 5, 5, 4]
    corridors_list= [[[1,2],[5,2],[4,1],[2,4],[3,1],[3,4]],
                      [[1,2],[3,4]],
                      [[1,2],[5,2],[4,1], [3,1],[3,4]],
                      [[1,2],[5,2],[4,1],[2,4],[3,1],[3,4],[1,5]],
                      [[1,2], [2,3], [3,4]]
                    ]

    for i in range(len(n_list)):
        print(i + 1, ".\tn: ", n_list[i], sep = "")
        print("\tcorridors: ", corridors_list[i], sep = "")
        print("\tcycles :", S.number_of_paths(n_list[i], corridors_list[i]))
        print("-"*100)


