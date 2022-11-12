class Solution:
    def isPalindrome(self, s: str) -> bool:
        lp, rp = 0, len(s) - 1
        while lp < rp:
            # skip non alfanumeric characters
            while not s[lp].isalnum() and lp < rp:
                lp += 1
            while not s[rp].isalnum() and lp < rp:
                rp -= 1
            # print(f'compare if {s[lp]} == {s[rp]}:')
            if s[lp].lower() != s[rp].lower():
                return False
            lp, rp = lp + 1, rp - 1
        return True


test_string = "A man, a plan, a canal: Panama"
testobject = Solution()
print(testobject.isPalindrome(test_string))
