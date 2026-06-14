"""
Diameter of Binary Tree — LeetCode 543 | Trees

Logic:
    The diameter through a node = left_height + right_height (edges, not nodes).
    DFS computes the height of each subtree bottom-up. At each node, update a
    running max with left + right. Return max(left, right) + 1 as the height.
    The answer is accumulated in self.result across all recursive calls.

Time:  O(n) — every node visited once
Space: O(h) — recursion stack
"""

from queue import deque
from q0_helpers import Node, BinaryTree

class Solution:
    def diameterofBinaryTree(self, node):
        self.result = 0
        def dfs(curr):
            if not curr:
                return 0
            left = dfs(curr.left)
            right = dfs(curr.right)
            self.result = max(self.result, left + right)
            return max(left, right) +1
        dfs(node)
        return self.result
    
    def diameterOfBinaryTree2(root):
        def helper(node):
            # returns (height, diameter)
            if not node:
                return 0, 0
            lh, ld = helper(node.left)
            rh, rd = helper(node.right)
            height = 1 + max(lh, rh)
            diameter = max(ld, rd, lh + rh)
            return height, diameter
    
        _, diameter = helper(root)
        return diameter

# Create and populate the tree
if __name__ == "__main__":
    tree = BinaryTree()
    values = [3,9,20,None,None,15,7]
    print("Inserting values:", values)
    for value in values:
        tree.insert_in_order(value)
    # Print the tree in different ways
    tree.print_tree()
    # Inverting Tree
    S = Solution()
    print(f"Diameter of the tree is {S.diameterofBinaryTree(tree.root)}")
    