import collections
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        result = collections.defaultdict(list)
        for s in strs:
            letter_map = [0] * (ord('z') +1 - ord('a'))
            for c in s:
                i = ord(c) -  ord('a')
                letter_map[i] += 1
            result[tuple(letter_map)].append(s)
        return result.values()

     

strs = ["eat","tea","tan","ate","nat","bat"]

test:Solution = Solution()
print(test.groupAnagrams(strs))