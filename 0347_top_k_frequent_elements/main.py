class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for i in nums:
            if i in counts:
                counts[i] += 1
            else:
                counts[i] = 1
        
        heap = []
        for i in counts:
            occurence = counts[i]
            heapq.heappush(heap, (-occurence, i))
        
        output = []
        for i in range(k):
            output.append(heapq.heappop(heap)[1])
        return output