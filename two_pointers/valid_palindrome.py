class Solution:
    def isPalindrome(self, s: str) -> bool:
        lp, rp = 0, len(s) - 1
        while lp < rp:
            if not s[lp].isalnum():
                lp +=1
            if not s[rp].isalnum():
                rp -= 1
            if s[lp].lower() != s[rp].lower():
                return False
            lp, rp = lp + 1, rp -1
        return True


test_string = "kajaK"
testobject = Solution()
print(testobject.isPalindrome(test_string))
