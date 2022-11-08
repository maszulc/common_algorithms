class Solution:
    def isValid(self, string: str) -> bool:
        Map = {")": "(", "]": "[", "}": "{"}
        stack = []

        for char in string:
            if char not in Map:
                stack.append(char)
                continue
            if not stack or stack[-1] != Map[char]:
                return False
            stack.pop()

        return not stack