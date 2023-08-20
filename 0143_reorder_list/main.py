# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        nodes = []
        while head:
            nodes.append(head)
            head = head.next
        
        l = 0
        r = len(nodes) - 1
        left = True

        while l < r:
            if left:
                nodes[l].next = nodes[r]
                l += 1
                left = False
            else:
                nodes[r].next = nodes[l]
                r -= 1
                left = True

            if l == r:
                if left:
                    nodes[l].next = None
                else:
                    nodes[r].next = None

        return nodes[0]