from typing import List

# Solution 2 - 100% Runtime and 87.35% memory
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        if nums is None:
            return []
        n = len(nums)
        candidate1, candidate2 = 0,0
        count_1, count_2 = 0, 0
        res = []
        for num in nums:
            if candidate1 == num:
                count_1 += 1
            elif candidate2 == num:
                count_2 += 1
            elif count_1 == 0:
                candidate1 = num
                count_1 = 1
            elif count_2 == 0:
                candidate2 = num
                count_2 = 1
            else:
                count_1 -= 1
                count_2 -= 1
        count_1, count_2 = 0,0
        for num in nums:
            if candidate1 == num:
                count_1 += 1
            elif candidate2 == num:
                count_2 += 1
        if count_1>n//3:
            res.append(candidate1)
        if count_2>n//3:
            res.append(candidate2)
        return res
    # Time complexity: O(n)
    # Space complexity: O(1)

# Solution 1 - 100% runtime and 87.37% memory
def majorityElement(nums: List[int]) -> List[int]:
    if nums is None:
        return []
    n = len(nums)
    if n <= 2:
        return list(set(nums))
    nums.sort()
    nums_n = []
    count = 1
    for i in range(1, n):
        if nums[i - 1] == nums[i]:
            count += 1
        else:
            if count > n // 3:
                nums_n.append(nums[i - 1])
            count = 1
        if len(nums_n) > 2:
            return nums_n
    if count > n // 3:
        nums_n.append(nums[-1])
    return nums_n
    # Time complexity: O(n log n) because of sorting
    # Space complexity: O(1)

# nums=[1]
# expected = [1]
# nums = [5,2,3,2,2,2,2,5,5,5]
# expected = [2, 5]
# nums=[4,4,4,4,4]
# expected=[4]