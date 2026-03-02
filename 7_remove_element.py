from typing import List
# Solution 4 - 100% runtime and 93.41% memory
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k]=nums[i] # move known non-value int to index with value
                k+=1
        return k
    # Time complexity: O(n)
    # Space complexity: O(1)

# Solution 3 - 82.68% runtime and 100% memory
# Cleaner version of solution 2 without .pop()
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i,k=0,len(nums)
        while i < k:
            if nums[i] == val:
                nums[i]=nums[k-1] # move known value int to last
                k-=1 # Shrink the space being searched
            else:
                i+=1
        return i
    # Time complexity O(n)
    # Space complexity O(1)

# Solution 2 - 100% runtime and 93.42% memory
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i,k=0,len(nums)-1
        while i <= k:
            if nums[i] != val:
                i+=1
            else:
                if nums[k] == val:
                    nums.pop() # remove last element if it is equal to val
                elif nums[i] == val:
                    nums[i]=nums[k] # move known value int to last
                    nums.pop() # delete last value
                k-=1
        return len(nums)
    # Time complexity O(n)
    # Space complexity

# Solution 1 -  100% runtime and 93.42% memory
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i, k = 0, 0
        n = len(nums) - 1
        while i <= n - k:
            if nums[i] == val:
                nums.pop(i) # O(n) complexity - can we do better?
                k += 1
            else:
                i += 1
        return len(nums)
    # Time complexity O(n^2) because of .pop(i)
    # Space complexity O(1)

# nums=[1,1,2,3,4] # expected: [2,3,4]
# val=1
# nums=[0,1,2,2,3,0,4,2] # expected [0,1,3,0,4]
# val=2
# nums=[1,1,1,1,1] # expected []
# val=1
# nums=[1] # expected []
# val=1