"""
Balanced Binary Tree — LeetCode 110 | Trees

Logic:
    DFS returns [is_balanced, height] for each subtree.
    A node is balanced if: both children are balanced AND |left_height - right_height| ≤ 1.
    This avoids a separate height computation — height and balance are derived in one pass.

Time:  O(n) — single DFS traversal
Space: O(h) — recursion stack
"""

from queue import deque
from q0_helpers import Node, BinaryTree

class Solution:
    def isBalanced(self, node):
        
        def dfs(node):
            if not node:
                return [True, 0]
            left, right = dfs(node.left), dfs(node.right)            
            balance = left[0] and right[0] and abs(left[1] - right[1]) <=1
            return [balance, 1 + max(left[1], right[1])]
        
        return dfs(node)[0]

    def isBalanced2(self, node):
        
        def dfs(node):
            if not node:
                return [True, 0]
            left = dfs(node.left)
            if not left[0]:
                return [False, 0]  # height doesn't matter anymore
            right = dfs(node.right)
            if not right[0]:
                return [False, 0] 
            balance = abs(left[1] - right[1]) <= 1
            return [balance, 1 + max(left[1], right[1])]        

        return dfs(node) != -1
# Create and populate the tree
if __name__ == "__main__":
    tree = BinaryTree()
    values = [1,2,2,3,3,None,None,4,4]
    # values = [1,2,2,3,3,5,6,4,4]
    print("Inserting values:", values)
    for value in values:
        tree.insert_in_order(value)
    # Print the tree in different ways
    tree.print_tree()
    # Inverting Tree
    S = Solution()
    print(f"Balanced Tree : {S.isBalanced(tree.root)}")
    