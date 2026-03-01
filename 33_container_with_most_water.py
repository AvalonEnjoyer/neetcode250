from typing import List

# Solution 1 - 100% Runtime and 100% Memory
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0  # two pointers
        j = len(heights) - 1
        max_area = 0
        while i < j:  # we are likely to maximize the area when the width is greater
            area = min(heights[i], heights[j]) * (j - i)
            max_area = max(max_area, area)
            if heights[i] < heights[j]:
                i += 1
            else:  # also catches when heights[i] == heights[j]
                j -= 1
        return max_area
    # Time complexity: O(n)
    # Space complexity: O(1)

# height=[1,7,2,5,4,7,3,6]
# expected = 36