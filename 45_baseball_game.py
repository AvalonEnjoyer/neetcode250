# Solution 1 - 100% runtime and 99.93% memory
class Solution:
    def calPoints(self, operations: List[str]) -> int:
        x = []
        for op in operations:
            if op == "+":
                x.append(x[-1]+x[-2])
            elif op=="C":
                x.pop()
            elif op=="D":
                x.append(x[-1]*2)
            else:
                x.append(int(op))
        return sum(x)