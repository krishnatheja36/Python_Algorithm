"""
Copy List With Random Pointer — LeetCode 2 | Linked List

Logic:
    Two-pass hashmap approach. oldToCopy maps each original node to its clone.
    Pass 1: create all clone nodes (values only), store in map.
    Pass 2: wire clone.next and clone.random using the map.
    None is pre-seeded in the map so random pointers to None resolve cleanly.

    Note: the second while loop is missing `cur = cur.next` — it loops forever.

Time:  O(n) — two passes
Space: O(n) — hashmap
"""

from q0_helpers import LinkedList, ListNode

class Solution:
    def copyRandomList(self, head:ListNode) -> ListNode:
        oldToCopy = {None: None}

        cur = head
        while cur:
            copy = ListNode(cur.val)
            oldToCopy[cur] = copy
            cur = cur.next

        cur = head
        while cur:
            copy = oldToCopy[cur]
            copy.next = oldToCopy[cur.next]
            copy.random = oldToCopy[cur.random]
        
        return oldToCopy[head]

if __name__ == "__main__":
    # Cant run this