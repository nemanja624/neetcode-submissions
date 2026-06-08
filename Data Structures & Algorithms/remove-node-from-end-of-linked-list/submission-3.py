# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        current = head
        count = 0
        i = 0

        while current:
            current = current.next
            count += 1

        current = head
        target = count - n 

        if target == 0:
            return head.next

        while current:
            if i == target - 1:
                current.next = current.next.next

            i += 1

            current = current.next

        return head