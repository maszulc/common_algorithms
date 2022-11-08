class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        t_count = {}
        s_count = {}
        for i in range(len(s)):
            t_count[t[i]] = t_count.get(t[i], 0) + 1
            s_count[s[i]] = s_count.get(s[i], 0) + 1
        return t_count == s_count
         
test = Solution()
s = "anagram"
t = "nagaram"
print(test.isAnagram(s, t))
s = "rat"
t = "car"
print(test.isAnagram(s, t))
