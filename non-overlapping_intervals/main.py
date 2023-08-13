class Solution:
    def eraseOverlapIntervals(self, intervals) -> int:
        intervals.sort()
        output = 0
        current_max = (-5 * 10 ** 4) - 1
        for i in intervals:
            if i[0] >= current_max:
                current_max = i[1]
            elif i[0] < current_max:
                output += 1
                current_max = min(current_max, i[1])
        return output