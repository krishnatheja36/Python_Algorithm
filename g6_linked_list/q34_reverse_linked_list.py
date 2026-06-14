"""
Reverse Linked List — LeetCode 206 | Linked List

Two approaches:

  1. reverseList — iterative:
       prev and curr pointers. At each step, store curr.next, redirect curr.next
       to prev, then advance both pointers. Return prev (new head).
       Time: O(n) | Space: O(1)

  2. reverseListRecurr — recursive:
       Recurse to the last node (new head). On the way back, redirect head.next.next
       to head and set head.next = None to sever the old forward link.
       Time: O(n) | Space: O(n) — call stack
"""

from q0_helpers import LinkedList, ListNode

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev, curr = None, head
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        return prev
    
    def reverseListRecurr(self, head: ListNode) -> ListNode:
        if not head:
            return None
        newHead = head
        if head.next:
            newHead = self.reverseListRecurr(head.next)
            head.next.next = head
        head.next = None

        return newHead


if __name__ == "__main__":
    head = [1,2,3,4,5]
    list1 = LinkedList()
    for data in head:
        list1.append(data)
    list1.print_list()
    S = Solution()
    list1.head = S.reverseList(list1.head)
    list1.print_list()
    list1.head = S.reverseListRecurr(list1.head)
    list1.print_list()