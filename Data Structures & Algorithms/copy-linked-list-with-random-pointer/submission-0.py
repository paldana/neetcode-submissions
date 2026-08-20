"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def __init__(self):
        self.map = {}   # key: original list node, val: deep copy node

    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return None
        if head in self.map:
            return self.map[head]
        
        copy = Node(head.val)
        self.map[head] = copy
        # perform recursion after saving the new copy node in the hashmap
        # to make sure all the nodes in the original list are already
        # created before we assign the new deep copy nodes' random 
        # pointers to their respective random index
        copy.next = self.copyRandomList(head.next) 
        copy.random = self.map.get(head.random)     
        return copy