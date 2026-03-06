from typing import List
# Solution 2 - 100% runtime and 100% memory
# Solution 1 - 78.29% runtime and 100% memory
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        max_profit = 0
        for i in range(1,len(prices)):
            max_profit += max(0, prices[i]-prices[i-1])
        return max_profit
    # Time complexity - O(n)
    # Space complexity - O(1)

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        max_profit = 0
        for i in range(1,len(prices)):
            profit = prices[i]-prices[i-1] if prices[i]-prices[i-1] > 0 else 0
            if profit != 0:
                max_profit += profit
        return max_profit
    # Time complexity - O(n)
    # Space complexity - O(1)

# prices = [7,1,5,3,6,4]
# expected = 7
