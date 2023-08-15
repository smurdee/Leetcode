class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        output = []

        for i, e in enumerate(nums):
            if i > 0 and e == nums[i-1]:
                continue
            
            if e < 1 and i + 2 < len(nums):
                l, r = i + 1, len(nums) - 1
                summ = e + nums[l] + nums[r]

                while l < r:
                    summ = e + nums[l] + nums[r]
                    if summ > 0:
                        r -= 1
                    elif summ < 0:
                        l += 1
                    else:
                        output.append([nums[i], nums[l], nums[r]])
                        l += 1
                        while nums[l] == nums[l-1] and l < r:
                            l += 1
                        
        
            else:
                return output

        return output