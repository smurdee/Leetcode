class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        headNode = ListNode()
        dummy = headNode
        for i, l in enumerate(lists):
            if l is not None:
                heap.append((l.val, i, l))

        heapq.heapify(heap)
        
        while heap:
            h_val, i, h = heapq.heappop(heap)
            dummy.next = h
            if h.next:
                heapq.heappush(heap, (h.next.val, i, h.next))
            dummy = dummy.next

        return headNode.next