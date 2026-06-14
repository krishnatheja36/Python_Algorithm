class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
class BinaryTree:
    def __init__(self):
        self.root = None
    
    def insert(self, value):
        """Insert a value into the binary search tree"""
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert_recursive(self.root, value)
    
    def insert_in_order(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return

        queue = [self.root]
        while queue:
            current = queue.pop(0)
            if current.left is None:
                current.left = new_node
                return
            else:
                queue.append(current.left)
            if current.right is None:
                current.right = new_node
                return
            else:
                queue.append(current.right)
        
    def _insert_recursive(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self._insert_recursive(node.left, value)
        else:
            if node.right is None:
                node.right = Node(value)
            else:
                self._insert_recursive(node.right, value)
    
    def print_tree(self):
        """Print the tree in multiple formats"""
        print("In-order traversal (Left -> Root -> Right):")
        self._inorder(self.root)
        print("\n")
        
        print("Pre-order traversal (Root -> Left -> Right):")
        self._preorder(self.root)
        print("\n")
        
        print("Post-order traversal (Left -> Right -> Root):")
        self._postorder(self.root)
        print("\n")
        
        print("Visual tree structure:")
        self._print_visual(self.root, "", True)
    
    def _inorder(self, node):
        if node:
            self._inorder(node.left)
            print(node.value, end=" ")
            self._inorder(node.right)
    
    def _preorder(self, node):
        if node:
            print(node.value, end=" ")
            self._preorder(node.left)
            self._preorder(node.right)
    
    def _postorder(self, node):
        if node:
            self._postorder(node.left)
            self._postorder(node.right)
            print(node.value, end=" ")
    
    def _print_visual(self, node, prefix="", is_tail=True):
        """Print tree in a visual format"""
        if node is not None:
            print(prefix + ("└── " if is_tail else "├── ") + str(node.value))
            
            children = []
            if node.left:
                children.append(node.left)
            if node.right:
                children.append(node.right)
            
            for i, child in enumerate(children):
                is_last = (i == len(children) - 1)
                extension = "    " if is_tail else "│   "
                
                if child == node.left and node.right:
                    self._print_visual(child, prefix + extension, False)
                else:
                    self._print_visual(child, prefix + extension, True)
