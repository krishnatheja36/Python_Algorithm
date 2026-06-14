"""
Flatten Binary Tree to Linked List — LeetCode 114 | Trees

Logic:
    Iterative Morris-style approach. For each node that has a left child, find the
    rightmost node of the left subtree, then attach the current node's right subtree
    to it. Move the left subtree to the right and set left to None. Advance to the
    right child and repeat.

Time:  O(n) — each node is visited at most twice (once as current, once as rightmost)
Space: O(1) — in-place flattening with no extra data structures
"""

from q0_helper_tree_dfs_utility import *


def flatten_tree(root):
    if not root:
        return
    
    current = root
    while current:
        if current.left:
            last = current.left
            
            while last.right:
                last = last.right
            
            last.right = current.right
            current.right = current.left
            current.left = None

        current = current.right
    return root


# driver code
if __name__ == '__main__':
    
    # Create a list of list of TreeNode objects to represent binary trees
    list_of_trees = [[TreeNode(3), TreeNode(2), TreeNode(17), TreeNode(1), TreeNode(4), TreeNode(19), TreeNode(5)],
                    [TreeNode(7), TreeNode(6), TreeNode(5), TreeNode(4), TreeNode(3), TreeNode(2), None, TreeNode(1)],
                    [TreeNode(5), TreeNode(4), TreeNode(6), TreeNode(3), TreeNode(2), TreeNode(7), TreeNode(8), TreeNode(1), TreeNode(9)],
                    [TreeNode(5), TreeNode(2), TreeNode(1), TreeNode(6), TreeNode(10), TreeNode(11), TreeNode(44)],
                    [TreeNode(1), TreeNode(2), TreeNode(5), TreeNode(3), TreeNode(4), TreeNode(6)],
                    [TreeNode(-1), TreeNode(-2), None, TreeNode(-5), TreeNode(1), TreeNode(2), TreeNode(-6)]
    ]

    # Create the binary trees using the BinaryTree class
    input_trees = []
    for list_of_nodes in list_of_trees:
        tree = BinaryTree(list_of_nodes)
        input_trees.append(tree)

    # Print the input trees
    x = 1
    for tree in input_trees:
        print(x, ".\tInput Tree:", sep = "")
        display_tree(tree.root)
        flatten_tree(tree.root)
        tree1 = flatten_tree(tree.root)
        print("\n\tFlattened tree:", sep="")
        display_tree(tree1)
        x += 1
        print("-" * 100)
