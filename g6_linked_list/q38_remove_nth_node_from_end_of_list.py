"""
Remove Nth Node From End of List — LeetCode 19 | Linked List

Logic:
    Use a dummy node before head to handle edge case of removing the head.
    Advance the right pointer n steps ahead of left. Then move both together
    until right reaches None — left.next is the node to remove.
    Set left.next = left.next.next to skip it.

Time:  O(n) — single pass
Space: O(1)
"""

from q0_helpers import LinkedList, ListNode

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0, head)
        left = dummy
        right = head
        while n>0 and right:
            right = right.next
            n -=1

        
        while right:
            left = left.next
            right = right.next
        
        left.next = left.next.next

        return dummy.next

if __name__ == "__main__":
    head = [1,2,3,4,5]
    n = 2
    list1 = LinkedList()
    for data in head:
        list1.append(data)
    print("Old List -", end= " ")
    list1.print_list()
    S = Solution()
    print(f"Removing {n}th node from end")
    S.removeNthFromEnd(list1.head, n)
    print("New List - ", end= " " )
    list1.print_list()
