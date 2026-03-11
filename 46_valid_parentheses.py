from typing import List
# Solution 2 - 100% runtime and 100% memory
class Solution:
    def isValid(self, s: str) -> bool:
        n = len(s)
        if n%2 != 0:
            return False
        stack=[]
        mapping = {")":"(", "}":"{", "]":"["}
        for char in s:
            if char in mapping:
                if not stack or mapping[char] != stack.pop():
                    return False
            else:
                stack.append(char)
        return not stack
    # Time complexity: O(n)
    # Space complexity: O(n)


# Solution 1 - 100% runtime and 100% memory
class Solution:
    def isValid(self, s: str) -> bool:
        n = len(s)
        if n%2 !=0:
            return False
        stack=[]
        for i in range(len(s)):
            if s[i] == '(' or s[i] == '[' or s[i] == '{':
                stack.append(s[i])
            else:
                if len(stack) == 0:
                    return False
                match s[i]:
                    case ')':
                        if stack.pop() == '(':
                            continue
                        else:
                            return False
                    case ']':
                        if stack.pop() == '[':
                            continue
                        else:
                            return False
                    case '}':
                        if stack.pop() == '{':
                            continue
                        else:
                            return False
        if len(stack)!=0:
            return False
        return True
    # Time complexity: O(n)
    # Space complexity: O(n)

# s = "[]"
# expected = True

# s = "([{}])"
# expected = True

# s = "[(])"
# expected = False