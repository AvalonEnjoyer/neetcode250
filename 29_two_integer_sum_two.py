from typing import List
# Solution 2: 100% runtime and 100% memory
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = len(numbers) - 1
        while i < j:
            sum = numbers[i] + numbers[j]
            if sum == target and numbers[i] != numbers[j]:
                return [i+1, j+1]
            elif sum > target:
                j -= 1
            elif sum < target:
                i += 1
    # Time complexity: O(n)
    # Space complexity: O(1)

# # Solution 1 - 100% runtime and 100% memory
# class Solution:
#     def twoSum(self, numbers: List[int], target: int) -> List[int]:
#         sum_map = {}
#         for index, number in enumerate(numbers):
#             complement = target - number
#             if number not in sum_map:
#                 sum_map[complement] = index+1
#             elif numbers[sum_map[number]-1] == number:
#                 continue
#             else:
#                 return [sum_map[number], index+1]
#     # Time complexity: O(n)
#     # Space complexity: O(n)

# numbers = [1, 2, 3, 4]
# target = 3
# print(twoSum(numbers, target))