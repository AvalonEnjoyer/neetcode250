from typing import List
# Solution 1 - 100% runtime and 81.21% memory
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        complements = {}
        for j, num in enumerate(nums):
            if num in complements and j-complements[num] <= k:
                return True
            complements[num] = j
        return False
    # Time complexity: O(n)
    # Space complexity: O(m) => O(n) in worst case scenarios with no unique elements


# nums = [1, 2, 3, 1]
# k = 3
# expected = True

# nums = [2,1,2]
# k = 1
# expected = False