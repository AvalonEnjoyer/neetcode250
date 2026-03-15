from typing import List
# Solution 2 - 100% runtime and 100% memory
# Use the combined sorted list of tuples
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse=True)
        fleets = []
        for p, s in cars:
            current_time = (target - p) / s

            if not fleets or current_time > fleets[-1]:
                fleets.append(current_time)

        return len(fleets)

# Solution 1 - 100% runtime and 100% memory
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        combined = sorted(zip(position, speed), reverse=True)
        position, speed = zip(*combined)
        time = []
        for i in range(len(position)):
            current_time = (target-position[i])/speed[i]
            if not time:
                time.append(current_time)
            else:
                if current_time not in time and not current_time<time[-1]:
                    time.append(current_time)
        print(time)
        return len(time)