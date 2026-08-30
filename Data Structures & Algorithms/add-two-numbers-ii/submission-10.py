# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    ## Stack Solution
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        s1, s2 = [], []


        # add LL vals to the stacks
        while l1:
            s1.append(l1.val)
            l1 = l1.next
        
        while l2:
            s2.append(l2.val)
            l2 = l2.next

        # Pop from the stacks to start from the end (least significant digits)
        head = None     # setup the head of the node - by the end of the loop, this will be the start of the result
        carry = 0
        while s1 or s2 or carry:
            num1 = s1.pop() if s1 else 0
            num2 = s2.pop() if s2 else 0
            sum = num1 + num2 + carry
            rem = sum % 10
            carry = sum // 10

            # set the linked list nodes - reversed
            curr = ListNode(rem)
            curr.next = head            # point to the previous node
            head = curr                 # set head as the node that was just created to be the new prev node in the next loop
        
        return head

    
    ## Reversed List Solution
    # Time and Space Complexities: O(n), where n is the length of the longer input linked list
    # def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    #     rl1 = self.reverseList(l1)
    #     rl2 = self.reverseList(l2)

    #     dummy = node = ListNode()
    #     carry = 0
        
    #     while rl1 or rl2 or carry:
    #         num1 = rl1.val if rl1 else 0
    #         num2 = rl2.val if rl2 else 0
    #         sum = num1 + num2 + carry

    #         rem = sum % 10
    #         carry = sum // 10
    #         node.next = ListNode(rem)

    #         node = node.next
    #         rl1 = rl1.next if rl1 else None
    #         rl2 = rl2.next if rl2 else None
        
    #     return self.reverseList(dummy.next)
            
    # def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    #     prev = None
    #     while head:
    #         temp = head.next
    #         head.next = prev
    #         prev = head
    #         head = temp
    #     return prev



