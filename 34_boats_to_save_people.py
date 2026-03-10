from typing import List

# Greedy solution
# Solution 2 -  99.95% runtime and 85.9% memory
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        res = 0
        j = len(people) -1
        i = 0
        while i <= j:
            if people[i] + people[j] <= limit:
                i+=1
            j-=1
            res+=1
        return res

# Solution 1 - 99.95% runtime and 100% memory
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        if people is None:
            return
        people.sort()
        res = 0
        n = len(people)
        i = 0
        j = n-1
        temp = 0
        while i <= j:
            if people[j] == limit:
                res += 1
                j -= 1
            else:
                if i == j:
                    res+=1
                    break
                temp = people[i] + people[j]
                if temp == limit:
                    res += 1
                    i+=1
                    j-=1
                elif temp > limit:
                    res += 1
                    j-=1
                else:
                    new_temp = people[i]+people[i+1]
                    if new_temp<limit:
                        i+=2
                    else:
                        i+=1
                        j-=1
                    res += 1
        return res

# people = [1,3,2,3,2]
# limit = 3
# expected = 4

# people=[5,1,4,2]
# limit=6
# expected = 2

# people=[5,1,4,2]
# limit=10
# expected = 2