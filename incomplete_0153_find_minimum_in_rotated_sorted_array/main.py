class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        output = 5001
        while left < right:
            index = (right + left) // 2
            output = min(output, nums[index])
            if nums[index] > nums[right]:
                left = index + 1
            else:
                right = index
        
        return min(output, nums[left])