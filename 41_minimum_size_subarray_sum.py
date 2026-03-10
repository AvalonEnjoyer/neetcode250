from typing import List
# Follow-up solution with O(n log(n)) complexity
# Solution 3: 87.64% runtime and 71.2% memory
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        import bisect
        n = len(nums)
        prefix = [0]*(n+1)
        for i in range(n):
            prefix[i+1] = prefix[i] + nums[i]
        print(nums)
        print(prefix)

        res = float('inf')
        for i in range(n):
            needed = prefix[i] + target
            j = bisect.bisect_left(prefix, needed)
            if j<=n:
                res=min(res,j-i)
        return 0 if res==float('inf') else res
    # Time complexity: O(n log(n))
    # Space complexity: O(n)


# Solution 2: 87.64% runtime and 100% memory
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minimum = float('inf')
        n = len(nums)
        left = 0
        right = 0
        window_sum = 0
        while right < n:
            window_sum += nums[right]
            if window_sum >= target:
                while window_sum - nums[left] >= target:
                    window_sum -= nums[left]
                    left += 1
                minimum = min(minimum, right-left+1)
            right += 1
        return  0 if minimum == float('inf') else minimum
    # Space complexity: O(n)
    # Time complexity: O(1)

# Solution 1: 100% runtime and 100% memory
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if nums is None:
            return 0
        minimum = 0
        n = len(nums)
        left = 0
        right = 0
        window_sum = 0
        while right < n:
            window_sum += nums[right]
            if window_sum >= target:
                while window_sum - nums[left] >= target:
                    window_sum -= nums[left]
                    left += 1
                minimum = right-left+1 if minimum==0 else min(minimum, right-left+1)
            right += 1
        return minimum
    # Space complexity: O(n)
    # Time complexity: O(1)