from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Solution 1 100% Runtime 97.31% Memory
        # sublists = []
        # char_maps = {}
        # for string in strs:
        #     ordered_string = "".join(sorted(string))
        #     if ordered_string not in char_maps:
        #         char_maps.setdefault(ordered_string, [string])
        #     else:
        #         char_maps[ordered_string].append(string)
        # for keys, values in char_maps.items():
        #     sublists.append(values)
        # return sublists

        # Time complexity - O(n*k log k)
        # Space - O(n*k)

        # Solution 2 100% runtime 97.31% Memory
        sublists = []
        char_maps = {}
        for string in strs:
            key = [0] * 26
            for char in string:
                key[ord(char) - ord("a")] += 1
            key = tuple(key)
            if key not in char_maps:
                char_maps.setdefault(key, [string])
            else:
                char_maps[key].append(string)
        for keys, values in char_maps.items():
            sublists.append(values)
        return sublists

        # Time complexity - O(n*k)
        # Space complexity - O(n)