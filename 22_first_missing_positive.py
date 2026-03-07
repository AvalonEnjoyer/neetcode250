from typing import List
# Solution 1 - 81.55% runtime and 78.94% memory
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            # Check number is between 1 and n and not already in place
            while 1 <= nums[i] <= n and nums[i] != nums[nums[i] - 1]:
                correct = nums[i] - 1
                nums[i], nums[correct] = nums[correct], nums[i]
                # Keep swapping until current index is negative or has the correct number
        for i in range(1, n + 1):
            if i != nums[i - 1]:
                return i  # First number that doesn't correspond to the index is the one missing
        return n + 1  # If all numbers are in order and placed according to their index

# nums = [-2,-1,0] # 1
# nums = [1,2,4] # 3
# nums = [1,2,4,5,6,3,1] # 7
# nums=[7,8,9,11,12] # 1
# nums=[3,4,-1,1] # 2
# nums = [2,3,4,5] # 1
# nums=[100,-1,-2,50,99,98]   # 1