class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        zeros = 0
        output = []
        for i in range(len(nums)):
            if i != (len(nums) - 1):
                if nums[i] == nums[i+1]:
                    nums[i] *= 2
                    nums[i+1] = 0
            if nums[i] == 0:
                zeros += 1
            else:
                output.append(nums[i])

        output += [0] * zeros

        return output