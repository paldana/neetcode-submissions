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
        copyMap = {None:None}    # key: orig node, val: copy node 
         # important to initialize None: None so it returns None when the random pointer is pointing to null
        

        print(copyMap)

        # 1st pass - create copy node and add to map
        cur = head
        while cur:
            copyNode = Node(cur.val)
            copyMap[cur] = copyNode
            cur = cur.next
        
        # 2nd pass - point the copy's next and random pointers to their respective copy nodes
        cur = head
        while cur:
            copy = copyMap[cur]
            copy.next = copyMap[cur.next]
            copy.random = copyMap[cur.random]
            cur = cur.next

        return copyMap[head]
