# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        current = head
        dups = {}

        while current:
            if current in dups:
                return True
            else:
                dups[current] = 1

            current = current.next

        return False