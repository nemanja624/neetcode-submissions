"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        current = head
        hashmap = {}

        while current:
            hashmap[current] = Node(current.val)
            current = current.next

        current = head

        while current:
            if current.random:
                hashmap[current].random = hashmap[current.random]

            if current.next:
                hashmap[current].next = hashmap[current.next]

            current = current.next

        return hashmap[head]
