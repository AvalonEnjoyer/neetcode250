from typing import List

# Solution 1 - 100% runtime and 98.63% memory
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        print(nums)
        # Break down the 4 sum problem to a three sum and two sum
        n = len(nums)
        res = []
        i = 0
        while i < n - 3:
            j = i + 1
            while j < n-2:
                temp_target = target - nums[i] - nums[j]
                left = j+1
                right = n-1
                while left < right:
                    if nums[left] + nums[right] == temp_target:
                        res.append([nums[i], nums[j], nums[left], nums[right]])
                        left += 1
                        right -= 1
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        while right > left and nums[right] == nums[right - 1]:
                            right -= 1
                    if nums[left] + nums[right] < temp_target:
                        left += 1
                    else:
                        right -= 1
                while j < n - 2 and nums[j + 1] == nums[j]:
                    j += 1
                j+=1
            while nums[i + 1] == nums[i] and i < n - 3:
                i+=1
            i+=1
        return res
    # Time complexity: O(n^3)
    # Space complexity: O(k)

# nums = [3,2,3,-3,1,0]
# target = 3
# expected =  [[-3,0,3,3],[-3,1,2,3]]
#
# nums = [1,-1,1,-1,1,-1]
# target = 2
# expected = [[-1,1,1,1]]

# nums=[1,0,-1,0,-2,2]
# target=0
# expected = [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]