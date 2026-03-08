from typing import List
# Solution 2 - 100% runtime and 98.32% memory
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        for j in range(1, len(nums)):
            if nums[i] != nums[j]:
                i+=1
                nums[i] = nums[j]
        return i+1
    # Time complexity: O(n)
    # Space complexity: O(1)

# Solution 1 - 100% runtime and 98.32% memory
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 1 # at least 1 unique element
        n = len(nums)
        i = 0
        j = 1
        while j < n:
            if nums[i] == nums[j]:
                j+=1
            else:
                i+=1
                k+=1
                nums[i] = nums[j]
                j+=1
        return k
    # Time complexity: O(n)
    # Space complexity: O(1)

# nums = [1,1,2,3,4]
# expected = [1,2,3,4] # k=4
# nums = [2,10,10,30,30,30]
# expected = [2,10,30] # k=3