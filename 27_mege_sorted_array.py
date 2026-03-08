from typing import List
# Optimal Solution
# Solution 2 - 100% runtime and 92.03% memory
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = m-1
        j = n-1
        k = m+n-1
        # Comparisons start from the right side so that the greater elements are placed first to the right
        while j>=0:
            if i >=0 and nums1[i]>nums2[j]:
                nums1[k] = nums1[i]
                i-=1
            else:
                nums1[k] = nums2[j]
                j-=1
            k-=1
            # Time complexity: O(m+n)
            # Space complexity: O(1)

# Wrong solution
# Solution 1 - 100% runtime and 92.04% memory
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i, j = 0, 0
        while i<len(nums1) and j<len(nums2):
            m-=i
            if nums1[i] == 0 and i>=m:
                nums1[i] = nums2[j]
                j+=1
            elif nums1[i] > nums2[j]:
                k = len(nums1)-1
                while k > i:
                    nums1[k] = nums1[k-1]
                    k -= 1
                nums1[i] = nums2[j]
                j+=1
            i+=1
            # Time complexity: O(n^2)
            # Space complexity: O(1)

# nums1 = [10,20,20,40,0,0]
# m = 4
# nums2 = [1,2]
# n = 2
# expected = [1,2,10,20,20,40]

# nums1 = [0,0]
# m = 0
# nums2 = [1,2]
# n = 2
# expected=[1,2]