class Solution:
    def getXORSum(self, arr1, arr2) -> int:
        left = arr1[0]
        right = arr2[0]
        for i in range(1, len(arr1)):
            left ^= arr1[i]
        for i in range(1, len(arr2)):
            right ^= arr2[i]
        
        output = left & right
        return output

# Debug
test = Solution()
print(test.getXORSum([12], [4]))