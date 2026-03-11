from typing import List

# Solution 1 - 79.17% runtime and 100% memory
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        n = len(arr)
        left, right = 0, n-k
        while left < right:
            mid = left + (right - left) // 2
            if abs(x-arr[mid])>abs(arr[mid+k]-x):
                left = mid + 1
            else:
                right = mid
        return arr[left:left+k]

# arr=[-10,-5,0,5,10]
# k=3
# x=1
# expected=[-5,0, 5]

# arr=[1,2,3,4,5]
# k=4
# x=-1
# expected = [1,2,3,4]

# arr=[1,2,3,4,5]
# k=4
# x=10
# expected = [2,3,4,5]

# arr=[1,3,5,7,9]
# k=3
# x=6
# expected = [3,5,7]
#
# arr = [2,4,5,8]
# k = 2
# x = 6
# expected = [4,5]
#
# arr = [1,1,2,3]
# k = 3
# x = 2
# expected = [1,1,2]
#
# arr = [2,3,4]
# k = 3
# x = 1
# expected = [2,3,4]
#
# arr=[1,2,3,4,5]
# k=4
# x=3
# expected=[1,2,3,4]
#
# arr=[5,10,15,20,25]
# k=1
# x=13
# expected=[15]