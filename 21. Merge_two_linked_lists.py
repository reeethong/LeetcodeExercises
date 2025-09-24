# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 == None: #base cases
            return list2
        if list2 == None:
            return list1
        cur = temp = ListNode()
        while list1 and list2:
            if list1.val <= list2.val:
                temp.next = list1
                list1 = list1.next
                temp = temp.next
            else:
                temp.next = list2
                temp = temp.next
                list2 = list2.next
        if list1: #check if either list still has nodes at the end
            temp.next = list1
        else:
            temp.next = list2
        return cur.next
