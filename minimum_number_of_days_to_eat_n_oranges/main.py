class Solution:
    def minDays(self, n: int) -> int:
        minimum_days = 0
        while (n != 0):
            if ((n/2) % 2 == 0):
                n /= 2
            elif ((n-1) % 3 == 0):
                n -= 1
            elif (n % 3 == 0):
                n /= 3
            elif (n % 2 == 0):
                n /= 2
            else:
                n -= 1
            minimum_days += 1
        return minimum_days

## Debug
test = Solution()
print(test.minDays(6))