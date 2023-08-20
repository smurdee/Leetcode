class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        nodes = []
        while head:
            nodes.append(head)
            head = head.next
        
        length = len(nodes)

        if n != length:
            if n != 1:
                nodes[-n-1].next = nodes[-n + 1]
            else:
                nodes[-n-1].next = None
        elif n == length:
            nodes = nodes[1:]
        
        if length == 1:
            return None
        else:
            return nodes[0]