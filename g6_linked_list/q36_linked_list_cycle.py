"""
Linked List Cycle — LeetCode 141 | Linked List

Logic:
    Floyd's tortoise and hare algorithm. slow moves 1 step, fast moves 2.
    If there is a cycle, fast will eventually lap slow and they will meet.
    If fast reaches None (or fast.next is None), the list is acyclic.

Time:  O(n) — fast catches slow within one loop cycle
Space: O(1) — two pointers only
"""

from q0_helpers import LinkedList, ListNode

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
       
        return False

if __name__ == "__main__":
    head = [1,2,3,4,5]
    list1 = LinkedList()
    for data in head:
        list1.append(data)
    list1.print_list()
    S = Solution()
    print("Given list has cycle", S.hasCycle(list1.head))
    
