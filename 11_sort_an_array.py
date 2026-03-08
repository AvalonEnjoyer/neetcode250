from typing import List
import heapq

# Solution 5 - 100% runtime and 95.74% memory
# Heapsort
def sortArray(nums: List[int]) -> List[int]:
    # To heapify a subtree rooted with node i
    def heapify(arr, n, i):
        # Initialize largest as root
        largest = i
        # left index = 2*i + 1
        l = 2 * i + 1
        # right index = 2*i + 2
        r = 2 * i + 2
        # If left child is larger than root
        if l < n and arr[l] > arr[largest]:
            largest = l
        # If right child is larger than largest so far
        if r < n and arr[r] > arr[largest]:
            largest = r
        # If largest is not root
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            # Recursively heapify the affected sub-tree
            heapify(arr, n, largest)

    n = len(nums)
    # Build heap (rearrange vector)
    for i in range(n // 2 - 1, -1, -1):
        heapify(nums, n, i)
    print(nums)
    # One by one extract an element from heap
    for i in range(n - 1, 0, -1):
        # Move current root to end
        nums[0], nums[i] = nums[i], nums[0]
        # Call max heapify on the reduced heap
        heapify(nums, i, 0)

    return nums

# Solution 4 - 82.8% runtime and 95.74% memory
# MergeSort
# def sortArray(nums: List[int]) -> List[int]:
#     def merge(left, right):
#         res = []
#         i, j = 0, 0
#         while i < len(left) and j < len(right):
#             if left[i] < right[j]:
#                 res.append(left[i])
#                 i += 1
#             else:
#                 res.append(right[j])
#                 j += 1
#         res.extend(left[i:])
#         res.extend(right[j:])
#         return res
#
#     def mergesort(arr: List[int]):
#         if len(arr) <= 1:
#             return arr
#         mid = len(arr) // 2
#         left = mergesort(arr[:mid])
#         right = mergesort(arr[mid:])
#         return merge(left, right)
#
#     return mergesort(nums)


# # Counting sort Doesn't work here because negative numbers
# def sortArray(nums: List[int]) -> List[int]:
#     count_array = [0]*(max(nums)+1)
#     n = len(nums)
#     for num in nums:
#         count_array[num] += 1 # Count frequency of each element
#
#     # Python allows for dynamic arrays hence the following
#     ans_array = []
#     for i, num in enumerate(count_array):
#         for j in range(num):
#             ans_array.append(i)
#
#     # If we had to use static arrays
#     # ans_array = [0]*n
#     # index = 0
#     # for i, num in enumerate(count_array):
#     #     for j in range(num):
#     #         ans_array[index] = i
#     #         index += 1
#     return ans_array
#     # Time complexity: O(n+k) - worst case
#     # Space complexity: O(k)

# Solution 3 - 70.73% runtime and 100% memory
# # Bubble sort
# def sortArray(nums: List[int]) -> List[int]:
#     n = len(nums)
#     count = 0
#     for i in range(n):
#         swapped = False
#         for j in range(0, n-i-1):
#             if nums[j] > nums[j+1]:
#                 count+=1
#                 nums[j], nums[j+1] = nums[j+1], nums[j]
#                 swapped = True
#         if not swapped:
#             break
#     return nums
#     # Time complexity: O(n^2)
#     # Space complexity: O(1)

# Solution 2 - 71.95% runtime and 95.74% memory
# # Insertion sort
# def sortArray(nums: List[int]) -> List[int]:
#     n = len(nums)
#     for i in range(1,n):
#         j = i-1
#         key = nums[i]
#         while j>=0 and nums[j]>key:
#             nums[j+1] = nums[j]
#             j -= 1
#         nums[j+1] = key
#     return nums
# #     # Time complexity: O(n^2) in worst case
# #     # Space complexity: O(1)

# Solution 1 - 82.82% runtime and 95.73% memory
# # Selection sort
# def sortArray(nums: List[int]) -> List[int]:
#     n = len(nums)
#     for i in range(n-1):
#         lowest_index = i
#         for j in range(i+1, n):
#             if nums[j] < nums[lowest_index]:
#                 lowest_index = j
#         nums[i], nums[lowest_index] = nums[lowest_index], nums[i]
#     return nums
#     # Time complexity: O(n^2)
#     # Space complexity: O(1)

# nums=[5,10]
# nums = [5,10,2,1,3]
# expected = [1,2,3,5,10]
# nums = [10,9,1,1,1,2,3,1]
# expected = [1,1,1,1,2,3,9,10]