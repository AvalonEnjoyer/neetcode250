from typing import List

# Solution 1 - 80.39% runtime and 76.38% memory
# Counting sort
def sortColors( nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    freq = [0] * 3
    for num in nums:
        freq[num] += 1
    count = 0
    for i, count_i in enumerate(freq):
        for _ in range(count_i):
            nums[count] = i
            count += 1
    return nums
    # Time Complexity: O(n)
    # Space Complexity: O(1)

# Solution 2 - 80.4 % runtime and 74.38% memory
# Dutch national flag algorithm
def sortColors( nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    low = 0
    mid = 0
    high = len(nums) - 1
    while mid <= high:
        if nums[mid] == 0:
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1
            mid += 1
        elif nums[mid] == 2:
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1
        elif nums[mid] == 1:
            mid += 1
    return nums
    # Time Complexity: O(n)
    # Space Complexity: O(1)

# nums = [1,0,1,2]
# expected = [0,1,1,2]
# nums=[0,1,2,2,1,0,1,2,0]
# expected = [0,0,0,1,1,1,2,2,2]
# nums = [2,1,0]
# expected = [0,1,2]