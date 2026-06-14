"""
Invert Binary Tree — LeetCode 226 | Trees

Logic:
    Recursively swap the left and right children at every node (post-order not needed —
    swapping at current node before recursing also works since we visit all nodes).
    Base case: if node is None, return None.

Time:  O(n) — every node visited once
Space: O(h) — recursion call stack; h = tree height (O(log n) balanced, O(n) worst)
"""

from q0_helpers import Node, BinaryTree

class Solution:
    def invertTree(self, node):
        if node:
            node.left, node.right = node.right, node.left
            self.invertTree(node.left)
            self.invertTree(node.right)
        

# Create and populate the tree
if __name__ == "__main__":
    tree = BinaryTree()
    values = [50, 30, 70, 20, 40, 60, 80, 10, 25, 35, 65]
    print("Inserting values:", values)
    for value in values:
        tree.insert(value)
    # Print the tree in different ways
    tree.print_tree()
    # Inverting Tree
    S = Solution()
    S.invertTree(tree.root)
    # Print after invert
    tree.print_tree()