"""
Reorder List — LeetCode 143 | Linked List

Logic (three steps, all in-place):
  1. Find the midpoint using slow/fast pointers; split into two halves.
  2. Reverse the second half in-place.
  3. Interleave nodes from the first half and reversed second half alternately.

Example: 1→2→3→4→5 becomes 1→5→2→4→3

Time:  O(n) — three linear passes
Space: O(1) — no extra data structures
"""

from q0_helpers import LinkedList, ListNode

class Solution:
    def reorderList(self, head: ListNode) -> None:
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second = slow.next
        prev, slow.next = None, None
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp
            
        first, second = head, prev
        while second:
            temp1, temp2 = first.next, second.next
            first.next = second
            second.next = temp1
            first = temp1
            second = temp2


if __name__ == "__main__":
    head = [1,2,3,4,5]
    list1 = LinkedList()
    for data in head:
        list1.append(data)
    list1.print_list()
    S = Solution()
    S.reorderList(list1.head)
    list1.print_list()
