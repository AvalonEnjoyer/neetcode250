from typing import List

# Solution 1 - 1005 runtime and 100% memory
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token[-1].isnumeric():
                stack.append(int(token))
            else:
                x = stack.pop()
                y = stack.pop()
                if token=="+":
                    stack.append(y+x)
                elif token=="-":
                    stack.append(y-x)
                elif token=="*":
                    stack.append(y*x)
                else:
                    stack.append(int(y/x))
        return stack[0]

tokens=["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
