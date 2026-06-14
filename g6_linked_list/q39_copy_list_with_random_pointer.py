"""
Add Two Numbers — LeetCode 138 | Linked List

Logic:
    Simulate digit-by-digit addition from the least significant digit (head).
    Use divmod(val, 10) to split into carry and digit. Advance both list pointers
    (or treat exhausted list as 0). Continue while either list has nodes or carry remains.

Time:  O(max(m, n)) — length of the longer list
Space: O(max(m, n)) — result list
"""

from q0_helpers import LinkedList, ListNode

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(None)
        cur = dummy

        carry = 0
        while l1 or l2 or carry:
            v1 = l1.data if l1 else 0
            v2 = l2.data if l2 else 0
            val = v1 + v2 + carry
            carry, val = divmod(val, 10)
            
            cur.next = ListNode(val)

            cur = cur.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        
        return dummy.next

if __name__ == "__main__":
    l1 = [2,4,3]
    l2 = [5,6,4]
    List1 = LinkedList()
    List2 = LinkedList()
    List3 = LinkedList()
    for data in l1:
        List1.append(data)
    for data in l2:
        List2.append(data)
    
    List1.print_list()
    List2.print_list()
    S = Solution()
    List3.head = S.addTwoNumbers(List1.head, List2.head)
    List3.print_list()
