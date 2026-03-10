from typing import List
# Solution 2 - 100% runtime and 100% memory
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return
        n = len(nums)
        k = k % n
        def reverse(l, r):
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1
        reverse(0,n-1)
        reverse(0,k-1)
        reverse(k,n-1)
        # Time complexity: O(n)
        # Space complexity: O(1)

# Solution 1 - 100% runtime and 100% memory
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k%n
        nums[:n-k], nums[-k:] =nums[-k:], nums[:n-k]
    # Time complexity: O(n)
    # Space complexity: O(n) because in Python slicing creates a new list in memory
