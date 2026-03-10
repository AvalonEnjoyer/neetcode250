from typing import  List
# Solution 3: 100% runtime and 100% memory
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1 = len(s1)
        n2 = len(s2)
        if n2 < n1:
            return False
        char_map = [0]*26
        for char in s1:
            char_map[ord(char)-ord("a")] += 1
        temp = [0]*26
        # Build the first window to window-1 space
        for i in range(n1-1):
            temp[ord(s2[i]) - ord("a")] += 1
        for right in range(n1, len(s2)+1):
            left = right - n1
            temp[ord(s2[right-1]) - ord("a")] += 1
            if temp == char_map:
                return True
            temp[ord(s2[left]) - ord("a")] -= 1
        return False
    # TIme complexity: O(n2)
    # Space complexity: O(1)

# Solution 2: 100% runtime and 100% memory
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1 = len(s1)
        n2 = len(s2)
        if n2 < n1:
            return False
        char_map = [0]*26
        for char in s1:
            char_map[ord(char)-ord("a")] += 1
        temp = [0]*26

        for right in range(n1, n2+1):
            left = right - n1
            if left == 0:
                for i in range(left, right):
                    temp[ord(s2[i]) - ord("a")] += 1
            else:
                temp[ord(s2[right-1]) - ord("a")] += 1
            if temp == char_map:
                return True
            temp[ord(s2[left]) - ord("a")] -= 1
        return False
    # Time complexity: O(n2)
    # Space complexity: O(1)

# Solution 1: 100% runtime and 100% memory
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        included = False
        char_map = [0]*26
        for char in s1:
            char_map[ord(char)-ord("a")] += 1
        n1 = len(s1)
        n2 = len(s2)
        if n2 < n1:
            return False
        temp = {}
        for right in range(n1, n2+1):
            left = right - n1
            if left == 0:
                for i in range(left, right):
                    key = ord(s2[i]) - ord("a")
                    temp[key] = temp.get(key,0) + 1
            else:
                key = ord(s2[right-1]) - ord("a")
                temp[key] = temp.get(key, 0) + 1
            for key, value in temp.items():
                if char_map[key] == value:
                    included = True
                else:
                    included = False
                    break
            if included:
                return True
            if temp[ord(s2[left]) - ord("a")] != 0:
                temp[ord(s2[left]) - ord("a")] -= 1
            else:
                del temp[ord(s2[left]) - ord("a")]
        return included
    # Time complexity: O(n2)
    # Space complexity: O(1)

# s1 = "abc"
# s2 = "lecabee"
# expected = True

# s1 = "abc"
# s2 = "lecaabee"
# expected = False