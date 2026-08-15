# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        s1, s2 = [], []
        # get the values from the linked lists - most significant digit at index 0
        while l1:
            s1.append(l1.val)
            l1 = l1.next
        while l2:
            s2.append(l2.val)
            l2 = l2.next
        
        # add the 2 stacks together - starting from the top of the stacks -- least significant digits
        head = None
        carry = 0
        while s1 or s2 or carry:
            num1 = s1.pop() if s1 else 0
            num2 = s2.pop() if s2 else 0
            total = num1 + num2 + carry
            carry = total // 10
            rem = total % 10
            # create new node and link the node accordingly
            node = ListNode(rem)    
            node.next = head        
            head = node

        # by the end of the while-loop, the head will be pointing to the most significant digit of the sum of two lists
        return head

## Stack Method ##
# Time & Space Complexity
# Time complexity: O(m+n)
# Space complexity: O(m+n)
# where m and n are the lengths of l1 and l2, respectively

