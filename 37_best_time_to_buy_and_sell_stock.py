from typing import List

# Solution 2 - 100% runtime and 100% memory
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        last_min = float('inf')
        max_profit = 0
        for i in range(0, len(prices)):
            last_min = min(last_min, prices[i])
            max_profit = max(max_profit, prices[i] - last_min)
        return max_profit
    # Time complexity: O(n)
    # Space complexity: O(1)


# Solution 1- 100% runtime and 100% memory
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        last_min = float('inf')
        max_profit = 0
        for i in range(0, len(prices)):
            if prices[i] < last_min:
                last_min = prices[i]
            else:
                max_profit = max(max_profit, prices[i] - last_min)
        return max_profit
    # Time complexity: O(n)
    # Space complexity: O(1)
# prices=[2,1,2,1,0,1,2]
# expected = 2
# prices = [10, 8, 7, 5, 2]
# expected = 0
# prices = [10,1,5,6,7,1]
# expected = 6
# prices = [5,1,5,6,7,1,10]
# expected = 9
# prices=[7,1,5,3,6,4]
# expected=5