class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

    def __repr__(self):
        return f"Node({self.val})"

class Graph:
    def __init__(self):
        self.root = None

    def build_graph(self, adjList):
        # step 1 — create all nodes first
        nodes = {i + 1: Node(i + 1) for i in range(len(adjList))}

        # step 2 — assign neighbors
        for i, neighbors in enumerate(adjList):
            nodes[i + 1].neighbors = [nodes[n] for n in neighbors]

        self.root = nodes[1]

    def print_graph(self, node=None, visited=None):
        if node is None:
            node = self.root
        if visited is None:
            visited = set()
        if node.val in visited:
            return
        visited.add(node.val)
        print(f"{node} -> {node.neighbors}")
        for neighbor in node.neighbors:
            self.print_graph(neighbor, visited)

if __name__ == "__main__":
    g = Graph()
    adjList = [[2, 4], [1, 3], [2, 4], [1, 3]]
    g.build_graph(adjList)
    g.print_graph()
