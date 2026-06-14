"""
Maximum Depth of Binary Tree — LeetCode 104 | Trees

Three approaches:

  1. maxdepthDFSRec — recursive DFS:
       1 + max(left_depth, right_depth). Base: None → 0.
       Time: O(n) | Space: O(h)

  2. maxdepthBFS — level-order BFS:
       Process level by level; increment depth counter for each level.
       Time: O(n) | Space: O(w) — w = max width of tree

  3. maxdepthDFSIter — iterative DFS with explicit stack:
       Stack stores (node, current_depth) pairs; track max depth seen.
       Time: O(n) | Space: O(h)
"""

from queue import deque
from q0_helpers import Node, BinaryTree

class Solution:
    def maxdepthDFSRec(self, node):
        if not node:
            return 0
        return 1 + max(self.maxdepthDFSRec(node.left), self.maxdepthDFSRec(node.right))
    
    def maxdepthBFS(self, node):
        if not node:
            return 0
        level = 0
        q = deque([node])
        while q:
            for i in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            level +=1
        return level
    
    def maxdepthDFSIter(self, node):
        if not node:
            return 0
        stack = [[node,1]]
        res = 1
        while stack:
            node, depth = stack.pop()            
            if node:
                res = max(res, depth)
                stack.append([node.left, depth+1])
                stack.append([node.right, depth+1])
        
        return res

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
    print(f"Max depth of a Binary tree is : {S.maxdepthDFSRec(tree.root)}")
    print(f"Max depth of a Binary tree is : {S.maxdepthBFS(tree.root)}")
    print(f"Max depth of a Binary tree is : {S.maxdepthDFSIter(tree.root)}")
    