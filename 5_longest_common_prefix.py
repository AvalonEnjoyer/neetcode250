from typing import List

# Solution 3 - Vertical scanning 100% runtime and 77.15% memory
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if strs is None or len(strs) == 0:
            return ''
        if len(strs) == 1:
            return strs[0]
        elif len(strs[0]) == 1:
            return strs[0]
        # Base comparisons on the smallest word
        min_len = min(len(str) for str in strs)

        for i in range(min_len):
            char = strs[0][i]
            for j in range (1,len(strs)):
                if strs[j][i] != char:
                        return strs[0][:i]
        return strs[0][:min_len]
    # Time complexity: O(n)
    # Space complexity: O(1)

# Solution 2 Binary search - 80.45% runtime and 100% memory
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if strs is None or len(strs) == 0:
            return ''
        if len(strs) == 1:
            return strs[0]
        elif len(strs[0]) == 1:
            return strs[0]
        # Base comparisons on the smallest word
        min_len = min(len(str) for str in strs)

        # Improvement over solution 1 - now compares sliced string as a whole vs. each character
        def check_common_prefix(index):
            # Check if every string's character matches up to the given index
            for i in range(1, len(strs)):
                if strs[i][:index] != strs[0][:index]:
                    return False
            return True

        low = 1
        high = min_len
        while low <= high:
            mid = (high + low) // 2
            if check_common_prefix(mid):
                low += 1
            else:
                high -= 1
        return strs[0][:high]
    # Time complexity - O(n m log m)
    # Space complexity - O(m)

# Solution 1 Binary search - 80.45% runtime and 77.16% memory
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if strs is None or len(strs) == 0:
            return ''
        if len(strs) == 1:
            return strs[0]
        elif len(strs[0]) == 1:
            return strs[0]
        # Base comparisons on the smallest word
        min_len = min(len(str) for str in strs)

        def check_common_prefix(index):
            # Check if every string's character matches up to the given index
            for i in range(1, len(strs)):
                for j, char in enumerate(strs[i][:index]):
                    if char != strs[0][j]:
                        return False
            return True

        low = 1
        high = min_len
        while low<=high:
            mid = (high+low)//2
            if check_common_prefix(mid):
                low += 1
            else:
                high -= 1
        return strs[0][:high]


# strs = ["bat","bag","bank","band"]
# expected = "ba"
# strs=["interview","internet","internal","interval"]
# expected = "inter"
# strs = ["dance","dag","danger","damage"]
# expected = "da"
# strs=["flower","flow","flight"]
# expected = "fl"
# strs = ["neet","feet"]
# expected=""
# strs=["abc","abcde","abcdef"]
# expected = "abc"