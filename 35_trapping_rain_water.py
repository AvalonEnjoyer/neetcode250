from typing import List
def trap(height: List[int]) -> int:
    i = 0
    j = len(height) - 1
    boundary_j = 0
    boundary_i = 0
    area = 0
    while i < j:
        if height[i] < height[j]:
            if height[i] > boundary_i:
                boundary_i = height[i]
            else:
                area += boundary_i - height[i]
            i += 1
        else:
            if height[j] > boundary_j:
                boundary_j = height[j]
            else:
                area += boundary_j - height[j]
            j-=1
    return area
    # Time complexity: O(n)
    # Space complexity: O(1)

# # Solution 1 - 100% Runtime and 90% memory
# class Solution:
#     def trap(self, height: List[int]) -> int:
#         i = 0
#         j = len(height) - 1
#         boundary_j = height[j]
#         boundary_i = height[i]
#         area = 0
#         temp_count = 0
#         while i < j:
#             if boundary_i > boundary_j:
#                 j-=1
#                 if height[j] < boundary_j:
#                     temp_count += 1
#                     area += boundary_j - height[j]
#                 if height[j] >= boundary_j:
#                     temp_count = 0
#                     boundary_j = height[j]
#             else:
#                 i += 1
#                 if height[i] < boundary_i:
#                     temp_count += 1
#                     area += boundary_i - height[i]
#                 if height[i] >= boundary_i:
#                     temp_count = 0
#                     boundary_i = height[i]
#             if i >= j:
#                 boundary_difference = boundary_j-boundary_i if boundary_j>boundary_i else boundary_i-boundary_j
#                 area -= temp_count * boundary_difference
#         return area
    # Time complexity: O(n)
    # Space complexity: O(1)