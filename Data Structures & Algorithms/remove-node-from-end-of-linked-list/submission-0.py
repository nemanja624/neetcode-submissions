# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        current = head
        count = 0

        while current:
            count += 1
            current = current.next

        target = count - n
        i = 0

        if target == 0:
            return head.next

        current = head

        while current:
            if i == target - 1:
                current.next = current.next.next
            current = current.next
            i += 1

        return head

        