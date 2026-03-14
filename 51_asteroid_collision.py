from typing import List

# Solution 1 - 100% runtime and 92.43% memory
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        roids = []
        for c in asteroids:
            if not roids:
                roids.append(c)
            else:
                if (roids[-1] > 0) == (c > 0):
                    roids.append(c)
                else:
                    x = c
                    while roids and (roids[-1] > 0 )!= (x > 0):
                        y = roids.pop()
                        res = x+y
                        if res == 0:
                            x = 0
                            break
                        elif x>y:
                            x = x
                        else:
                            x = y
                    if x!=0:
                        roids.append(x)
        return roids

# Solution 2 - 76.53% runtime and 100% memory
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for c in asteroids: # if left comes after right - collision happens
            alive = True
            while stack and (stack[-1]>0) and (c<0) and alive:
                diff = stack[-1]+c
                if diff ==0:
                    alive = False
                    stack.pop()
                elif diff>0:
                    alive = False
                else:
                    stack.pop()
            if alive:
                stack.append(c)
        return stack

# asteroids=[10,2,-5]
# asteroids=[2,4,-4,-1]