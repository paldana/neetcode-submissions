# Definition for a Node.
# class Node:
#   def __init__(self, val=None, next=None):
#        self.val = val
#        self.next = next

class Solution:
    def insert(self, head: 'Optional[Node]', insertVal: int) -> 'Node':
        if not head:
            newNode = Node(insertVal)
            newNode.next = newNode
            return newNode
        
        prev, curr = head, head.next
        toInsert = False

        while True:
            # case 1 - insert new val between 2 nodes
            if prev.val <= insertVal <= curr.val:
                toInsert = True
            # case 2 - find a head-tail boundary and insert new min/max between them
            elif prev.val > curr.val:
                if insertVal >= prev.val or insertVal <= curr.val:
                    toInsert = True
            
            if toInsert:
                prev.next = Node(insertVal, curr)
                return head

            prev, curr = curr, curr.next

            # case 3 - a loop cycle detected - means all nodes have same value
            if prev == head:
                break
        
        # insert new node anywhere
        prev.next = Node(insertVal, curr)
        return head


            