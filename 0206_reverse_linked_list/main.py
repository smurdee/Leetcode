# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head
        
        ## basically you are rotating the direction of the pointers one by one and keeping
        ## track of the new_head and previous_head

        while curr:
            next_curr = curr.next # saving Node[2] as next_curr
            curr.next = prev # so that the direction can be rotated here
            prev = curr # prev now becomes Node[1]
            curr = next_curr # curr is now the next_curr Node[2]
            # in the next round of while loop, prev = Node[1], curr = Node[2]
        
        return prev