# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def reverseList(head):
            prev, curr = None, head
            while curr:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            return prev
        
        # rl1 the linked list first to make it easier to add
        rl1 = reverseList(l1)
        rl2 = reverseList(l2)
        head = None # head initially pointing to None as it will be next to the last node in the resulting list 
        carry = 0

        while rl1 or rl2 or carry :
            num1 = rl1.val if rl1 else 0
            num2 = rl2.val if rl2 else 0
            sum = num1 + num2 + carry   # calculate sum including carry
            node = ListNode(sum % 10)   # create new node with the val as the mod 10 of sum to get the single digit val
            carry = sum // 10           # carry will be the 2nd digit if the sum is a 2-digit val
            node.next = head        # point next pointer to the head node
            head = node             # move head pointer to the current node (moving backward in the resulting LL)
            
            # iterate to the next nodes in the reversed lists
            rl1 = rl1.next if rl1 else None
            rl2 = rl2.next if rl2 else None
        
        return head
    
# Time & Space Complexity
# Time complexity: O(m+n)
# Space complexity: O(max(m,n)) for the output list.
# Where m and n are the length l1 and l2, respectively
