from typing import List

# Solution 1 - 100% runtime and 99.94% memory
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum = {0:1} # one prefix with sum 0
        res = 0
        running_sum = 0
        for num in nums:
            running_sum += num
            diff = running_sum - k
            if diff in prefix_sum:
                res += prefix_sum[diff]
            prefix_sum[running_sum] = prefix_sum.get(running_sum, 0) + 1
        return res