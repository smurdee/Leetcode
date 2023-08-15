class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i,e in enumerate(prices):
            if i == 0 or e < buy:
                buy = e
                sell = e
            elif e > sell and e > buy:
                sell = e
                if (e - buy) > profit:
                    profit = e - buy
        return profit