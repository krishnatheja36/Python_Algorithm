"""
Compilation Order — Graphs / Topological Sort

Logic:
    Build a directed graph from dependency pairs (child depends on parent).
    Track in-degrees for each node. Start a BFS queue with all nodes that have
    in-degree 0 (no dependencies). Process each node, decrement its children's
    in-degrees, and enqueue children that reach 0. If the sorted order length
    equals the total number of nodes, no cycle exists.

Time:  O(V + E) — Kahn's topological sort processes each node and edge once
Space: O(V + E) — adjacency list and in-degree map
"""

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Compilation Order
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Statement
# There are a total of nn classes labeled with the English alphabet (AA, BB, CC, and so on). Some classes are dependent on other classes for compilation. For example, if class BB extends class AA, then BB has a dependency on AA. Therefore, AA must be compiled before BB.
# Given a list of the dependency pairs, find the order in which the classes should be compiled.
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Constraints:
# •	Class name should be an uppercase character.
# •	0≤0≤ dependencies.length ≤676≤676
# •	dependencies[i].length =2=2
# •	All dependency pairs should be unique.
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

from collections import defaultdict
from collections import deque


class Solution:
    def find_compilation_order(self, dependencies):

        dependency_list = defaultdict(list)
        indegree = defaultdict(int)
        sorted_order = []

        for dependency in dependencies:
            child, parent = dependency[0], dependency[1]
            dependency_list[parent].append(child)
            if parent not in indegree:
                indegree[parent] = 0
            indegree[child]+=1

        sources = deque()
        for key, val in indegree.items():
            if val == 0:
                sources.append(key)

        while sources:
            vertex = sources.popleft()
            sorted_order.append(vertex)
            for dep_vertex in dependency_list[vertex]:
                indegree[dep_vertex] -= 1
                if indegree[dep_vertex] == 0:
                    sources.append(dep_vertex)

        if len(indegree) == len(sorted_order):
            return sorted_order
        else:
            return []

if __name__ == '__main__':

    S = Solution()
    dependencies = [[['B', 'A'], ['C', 'A'], ['D', 'C'], ['E', 'D'], ['E', 'B']],
        [['B', 'A'], ['C', 'A'], ['D', 'B'], ['E', 'B'], ['E', 'D'], ['E', 'C'], ['F', 'D'], ['F', 'E'], ['F', 'C']],
        [['A', 'B'], ['B', 'A']],
        [['B', 'C'], ['C', 'A'], ['A', 'F']],
        [['C', 'C']]]
    for i in range(len(dependencies)):
        print(i + 1, ".\tdependencies: ", dependencies[i], sep = "")
        print("\tCompilation Order: ", S.find_compilation_order(dependencies[i]), sep = "")
        print("-"*100, "\n", sep ="")
