"""
Clone Graph — LeetCode 133 | Graphs

Logic:
    DFS with an oldToNew hashmap (original node → cloned node).
    If a node is already in the map, return its clone (handles cycles).
    Otherwise create a new clone, store it in the map, then recursively clone
    all neighbors and append them to the clone's neighbor list.

Time:  O(V + E) — each node and edge visited once
Space: O(V) — hashmap + recursion stack
"""

from q0_helper import Node, Graph

class Solution:
    def cloneGraph(self, node:Node) -> Node:
        oldToNew = {}
        
        def clone(node):
            if node in oldToNew:
                return oldToNew[node]
             
            copy = Node(node.val)
            oldToNew[node] = copy
            for nei in node.neighbors:
                copy.neighbors.append(clone(nei))
            return copy

        return clone(node) if node else None


if __name__ == "__main__":
    adjList = [[2,4],[1,3],[2,4],[1,3]]
    graph1 = Graph()
    graph1.build_graph(adjList)
    print("Graph 1")
    graph1.print_graph()
    graph2 = Graph()
    S = Solution()
    graph2.root = S.cloneGraph(graph1.root)
    print("Graph 2")
    graph2.print_graph()