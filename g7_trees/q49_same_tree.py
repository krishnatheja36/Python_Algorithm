"""
Same Tree — LeetCode 100 | Trees

Logic:
    Recursively compare both trees node by node.
    Both None → True (matching empty subtrees).
    One None, one not → False (structural mismatch).
    Values differ → False. Otherwise recurse on both left and right subtrees.

Time:  O(n) — visits every node in both trees
Space: O(h) — recursion stack (h = min height of the two trees in worst case)
"""

from queue import deque
from q0_helpers import Node, BinaryTree

class Solution:
    def isSameTree(self, p:Node, q:Node) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.value != q.value:
            return False

        left_check = self.isSameTree(p.left, q.left)
        right_check = self.isSameTree(p.right, q.right)

        return left_check and right_check

        # Condensed script
        # if not p and not q:
        #     return True
        # if not p or not q or p.value != q.value:
        #     return False
        # return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

# Create and populate the tree
if __name__ == "__main__":
    tree1 = BinaryTree()
    tree2 = BinaryTree()
    p = [1,2,3]
    # q = [1,2,3]
    q = [1,2,3, 4]
    # values = [1,2,2,3,3,5,6,4,4]
    for value in p:
        tree1.insert_in_order(value)
    for value in q:
        tree2.insert_in_order(value)

    # Print the tree in different ways
    tree1.print_tree()
    tree2.print_tree()
    # Inverting Tree
    S = Solution()
    print(f"Is it the Same tree : {S.isSameTree(tree1.root, tree2.root)}")
    