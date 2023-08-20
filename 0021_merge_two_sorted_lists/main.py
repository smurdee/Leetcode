# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        headNode = ListNode()
        dummy = headNode
        while list1 and list2:
            if list1.val <= list2.val:
                headNode.next = list1
                headNode = headNode.next
                list1 = list1.next
            else:
                headNode.next = list2
                headNode = headNode.next
                list2 = list2.next

        if list1:
            headNode.next = list1
        elif list2:
            headNode.next = list2
        
        return dummy.next