class ListNode:
    def __init__(self, data, next=None, random=None):
        self.data = data
        self.next = next
        self.random = random
        
class LinkedList:
    """A singly linked list implementation"""
    def __init__(self):
        self.head = None
    
    def append(self, data):
        """Add a new node at the end of the list"""
        new_node = ListNode(data)
        
        if not self.head:                   # If list is empty, make new node the head
            self.head = new_node
            return
        
        current = self.head                 # Traverse to the last node
        while current.next:
            current = current.next
        
        current.next = new_node             # Add new node at the end
    
    def prepend(self, data):                # Add a new node at the beginning of the list
        new_node = ListNode(data)
        new_node.next = self.head
        self.head = new_node
        
    
    def print_list(self):                   # Print all elements in the list
        if not self.head:
            print("List is empty")
            return
        
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")
    
    def insert_after(self, prev_data, data):                # Insert a new node after a node with given data"""
        current = self.head
        
        while current and current.data != prev_data:        # Find the node with prev_data
            current = current.next
        
        if not current:
            print(f"Node with data {prev_data} not found")
            return
        
        new_node = ListNode(data)                               # Insert new node
        new_node.next = current.next
        current.next = new_node

if __name__ == "__main__":
    ll = LinkedList()
    
    print("Creating linked list...")
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.append(4)
    
    print("Linked List:")
    ll.print_list()
    
    print("\nPrepending 0:")
    ll.prepend(0)
    ll.print_list()
    
    print("\nInserting 2.5 after 2:")
    ll.insert_after(2, 2.5)
    ll.print_list()
    
    print("\nCreating another list with strings:")
    ll2 = LinkedList()
    ll2.append("Apple")
    ll2.append("Banana")
    ll2.append("Cherry")
    ll2.print_list()

