from typing import List

# Solution 3 - 79.83% runtime and 94.67% memory
# Boyer-Moore approach
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        candidate = None
        for num in nums:
            if count == 0:
                candidate = num
            count += 1 if num == candidate else -1
        return candidate

# Solution 2 - 100% runtime and 100% memory
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        i = 0
        max_num = float('-inf')
        max_count = 0
        freq_map = {}
        while max_count <= n//2 and i < len(nums):
            freq_map[nums[i]] = freq_map.get(nums[i], 0) + 1
            if freq_map[nums[i]] > max_count:
                max_num = nums[i]
                max_count = freq_map[nums[i]]
            i += 1
        print(freq_map)
        return max_num
    # Time complexity - O(n)
    # Space complexity - O(m)

# Solution 1 - 79.84% runtime and 100% memory
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        i = 0
        max_count = 0
        freq_map = {}
        while max_count <= n//2 and i < len(nums):
            freq_map[nums[i]] = freq_map.get(nums[i], 0) + 1
            max_count = max(max_count, freq_map[nums[i]])
            i+=1
        for key, value in freq_map.items(): # this adds O(m) to time complexity compared to solution 2's approach
            if value == max_count:
                return key
        return None
    # Time complexity - O(n)
    # Space complexity - O(n)

# nums = [2,2,2] # expected = 2
# nums=[1,2,3,2,2,2,5,4,2] # expected = 2
# nums = [5,5,1,1,1,5,5] # expected = 5
