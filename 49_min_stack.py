# Solution 2 - 100% runtime and 100% memory
# min stack updates only when val >= last min
class MinStack:
    def __init__(self):
        self.min_stack = []
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self) -> None:
        if self.stack:
            if self.min_stack[-1] == self.stack.pop():
                self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]


# Solution 1 - 100% runtime and 100% memory
# min stack updates every push
class MinStack:
    from collections import deque
    def __init__(self):
        self.min_stack = []
        self.stack = []

    def push(self, val: int) -> None:
        if self.stack:
            self.min_stack.append(min(self.min_stack[-1], val))
        else:
            self.min_stack.append(val)
        self.stack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]
    # Time complexity: O(1)
    # Space complexity: O(n)

