from typing import List

# Solution 3 - 100% Runtime and 100% memory
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        max_length = 0
        for num in num_set:
            if num-1 not in num_set:
                current = num
                current_longest = 1

                while current+1 in num_set:
                    current += 1
                    current_longest += 1

                max_length = max(current_longest, max_length)
        return max_length
        # Time complexity: O(n)
        # Space complexity: O(n)

# # Solution 2 - 100% runtime and 100% memory
# class Solution:
#     def longestConsecutive(self, nums: List[int]) -> int:
#         if not nums:
#             return 0
#         nums.sort()
#         max_length = 1
#         current_longest = 1
#         for i in range(1,len(nums)):
#             if nums[i] == nums[i-1]:
#                 continue
#             elif nums[i] - nums[i-1] == 1:
#                 current_longest += 1
#             else:
#                 max_length = max(current_longest, max_length)
#                 current_longest = 1
#         return max(max_length,current_longest)
#         # Time complexity O(n log n)
#         # Space complexity O(n)

# # Solution 1 - 100% runtime and 100% memory
# class Solution:
#     def longestConsecutive(self, nums: List[int]) -> int:
#         nums.sort()
#         sequence_lengths = []
#         current_longest = 1
#         if len(nums) == 0:
#             return 0
#         for i, num in enumerate(nums):
#             if i != 0:
#                 if num == last_num:
#                     continue
#                 elif num - last_num == 1:
#                     current_longest += 1
#                 else:
#                     sequence_lengths.append(current_longest)
#                     current_longest = 1
#             last_num = num
#         sequence_lengths.append(current_longest)
#         return max(sequence_lengths)
#     # Time complexity O(n log n)
#     # Space complexity O(n)

# test = [2,20,4,10,3,4,5]
# print(longestConsecutive(test))