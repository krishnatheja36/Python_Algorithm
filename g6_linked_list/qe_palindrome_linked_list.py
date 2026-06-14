"""
Palindrome Linked List — LeetCode 234 | Linked List | Two Pointers

Logic:
    Use fast/slow pointers to find the midpoint of the list. Reverse the second
    half in-place, then compare the first half node-by-node with the reversed
    second half. Restore the list by reversing the second half again before returning.

Time:  O(n) — two passes through the list (finding mid + comparison)
Space: O(1) — reversal is done in-place with no extra data structures
"""

import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))
from p0_linkedlist_helper import *

class Solution:
    def palindrome(self, head):
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        revert_data = reverse_linked_list(slow)
        check = self.compare_two_halves(head, revert_data)

        reverse_linked_list(revert_data)

        return check

    def compare_two_halves(self,first_half, second_half):
        while first_half and second_half:
            if first_half.val != second_half.val:
                return False
            else:
                first_half = first_half.next
                second_half = second_half.next
        return True

if __name__ == "__main__":
    
    S = Solution()
    input = (
                [2, 4, 6, 4, 2],
                [0, 3, 5, 5, 0],
                [9, 7, 4, 4, 7, 9],
                [5, 4, 7, 9, 4, 5],
                [5, 9, 8, 3, 8, 9, 5],
            )
    j = 1

    for i in range(len(input)):
        input_linked_list = LinkedList()
        input_linked_list.create_linked_list(input[i])
        print(j, ".\tLinked List:", end=" ", sep="")
        print_list_with_forward_arrow(input_linked_list.head)
        head = input_linked_list.head
        print("\n\tIs it a palindrome?", "Yes" if S.palindrome(head) else "No")        
        j += 1
        print("-"*100, "\n")
	