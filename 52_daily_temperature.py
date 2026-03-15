from typing import List
# Solution 3 - 100% runtime and 100% memory
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0]*n
        stack = []
        for i in range(n): # when unresolved element in less than current temp
            while stack and temperatures[stack[-1]]<temperatures[i]:
                prev = stack.pop() # index of unresolved element
                res[prev]=i-prev # update res from 0 to i-prev
            stack.append(i) # index of the latest element always goes into the stack
        return res

# Solution 2 - 100% runtime and 100% memory
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0]*n
        for i in range(n-2, -1, -1):
            j = i+1
            while j<n and temperatures[j]<=temperatures[i]:
                if res[j] == 0: # Checking the res value for j to see if a greater element exists
                    j = n
                    break
                j += res[j] # jumping to the last value that was greater that temp[j]
            if j<n:
                res[i]=j-i
        return res

# Solution 2 - 100% runtime and 100% memory
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0]
        for i in range(n-2, -1, -1):
            j = i+1
            while j<n and temperatures[j]<=temperatures[i]:
                if res[n-1-j] == 0: # Checking the res value for temp[j] to see if a greater element exists
                    j = n
                    break
                j += res[n-1-j] # jumping to the last value that was greater that temp[j]
            if j<n:
                res.append(j-i)
            else:
                res.append(0)
        res.reverse()
        return res

# Solution 1 - 100% runtime and 100% memory
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0]
        for i in range(n-2, -1, -1):
            j = i+1
            while j<n-1 and temperatures[j]<=temperatures[i]:
                j+=1 # repeatedly check all previous values in the list
            if temperatures[j]>temperatures[i]:
                res.append(j-i)
            else:
                res.append(0)
        res.reverse()
        return res

# temperatures=[89,62,70,58,47,47,46,76,100,70]
