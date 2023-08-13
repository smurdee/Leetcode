import heapq

class Solution:
    def maxTwoEvents(self, events) -> int:
        heap = []; events.sort()
        result, maxVal = 0, 0
        for i in range(len(events)):
            while heap and heap[0][0] < events[i][0]:
                maxVal = max(maxVal, heapq.heappop(heap)[1])
            result = max(result, maxVal + events[i][2])
            heapq.heappush(heap, (events[i][1], events[i][2]))
        return result

answer = Solution()
events = [[1,3,2],[4,5,2],[2,4,3]]
print(answer.maxTwoEvents(events))