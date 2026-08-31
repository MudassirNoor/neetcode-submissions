# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res_head = ListNode(0, None)
        carry_over = 0
        n1 = l1
        n2 = l2
        
        next_res = res_head
        while n1 or n2 or carry_over:
            sum = 0
            sum += n1.val if n1 else 0
            sum += n2.val if n2 else 0
            
            if carry_over > 0:
                sum += carry_over
                carry_over = 0
            
            if sum > 9:
                carry_over = sum // 10
                sum = sum % 10
                
            next_res.next = ListNode(sum, None)
            next_res = next_res.next

            n1 = n1.next if n1 else None
            n2 = n2.next if n2 else None

        

        return res_head.next