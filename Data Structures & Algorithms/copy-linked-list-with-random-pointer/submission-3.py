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

        curr = head
        new_head = Node(curr.val, None, None)
        copy = new_head

        node_map = {}
        while curr:
            node_map[curr] = copy
            if curr.next:
                copy.next = Node(curr.next.val, None, None)
            
            copy = copy.next
            curr = curr.next


        curr = head
        copy = new_head

        while curr:
            if curr.random in node_map:
                copy.random = node_map[curr.random]
            curr = curr.next
            copy = copy.next

        return new_head