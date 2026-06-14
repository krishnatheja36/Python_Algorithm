"""
Merge Two Sorted Lists — LeetCode 21 | Linked List

Logic:
    Use a dummy head node to simplify edge cases. Maintain a tail pointer.
    Compare the fronts of both lists; attach the smaller node to tail and
    advance that list's pointer. After one list is exhausted, attach the rest
    of the other list directly (already sorted).

Time:  O(m + n) — each node visited once
Space: O(1) — in-place relinking, only dummy node allocated
"""

from q0_helpers import LinkedList, ListNode

class Solution:
    def mergeTwoLists(self, list1: [ListNode], list2: [ListNode]) -> [ListNode]:
        dummy = ListNode(None)
        tail = dummy

        while list1 and list2:
            if list1.data < list2.data:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2=list2.next
            tail = tail.next
        
        if list1:
            tail.next = list1
        if list2:
            tail.next = list2
        
        return dummy.next
            

if __name__ == "__main__":
    list1 = [1,2,4]
    list2 = [1,3,4]
    ll1 = LinkedList()
    ll2 = LinkedList()
    for data in list1:
        ll1.append(data)
    for data in list2:
        ll2.append(data)
    ll1.print_list()
    ll2.print_list()
    S = Solution()
    ll1.head =S.mergeTwoLists(ll1.head, ll2.head)
    ll1.print_list()