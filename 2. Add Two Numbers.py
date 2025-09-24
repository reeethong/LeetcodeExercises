# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        n1 = n2 = 0
        cur1 = l1
        i=0
        while cur1:
            n1 += cur1.val*10**i
            i += 1
            cur1 = cur1.next
        cur2 = l2
        j = 0
        n2 = 0
        while cur2:
            n2 += cur2.val*10**j
            j += 1
            cur2 = cur2.next
        
        sum1 = n1+n2
  
        current = result = ListNode()
        if sum1 == 0:
            return result
        while sum1>0:
            k = sum1%10
            current.next = ListNode(val=k)
            current = current.next
            sum1 = sum1 // 10

        return result.next
