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
            # case 1 - new value can be inserted between 2 nodes
            if prev.val <= insertVal <= curr.val:
                toInsert = True
            
            # case 2 - the new val is a new min. or max. (insert at the tail/head boundary)
            elif prev.val > curr.val:   # found the tail/head boundary
                if insertVal >= prev.val or insertVal <= curr.val:
                    toInsert = True
            
            if toInsert:
                prev.next = Node(insertVal, curr)
                return head
            
            # update pointers
            prev, curr = curr, curr.next

            # loop condition
            if prev == head:
                break
    
        # case 3 - all nodes have the same value, so insert the value anywhere
        prev.next = Node(insertVal, curr)
        return head