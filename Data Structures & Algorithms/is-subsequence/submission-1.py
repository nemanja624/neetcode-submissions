class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0:
            return True

        count = 0
        i = 0

        for char in t:
            if char == s[i]:
                count += 1
                i += 1

            if i == len(s):
                break

        if count == len(s):
            return True
        else:
            return False