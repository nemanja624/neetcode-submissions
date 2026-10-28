class Solution:

    def checkPalindrome(self, s: str):
        return s == s[::-1]

    def partition(self, s: str) -> List[List[str]]:
        if len(s) == 0:
            return []

        res = []
        path = []

        def backtrack(i: int):
            if i == len(s):
                res.append(path.copy())
                return

            for j in range(i, len(s)):
                if self.checkPalindrome(s[i:j+1]):
                    path.append(s[i:j+1])
                    backtrack(j + 1)
                    path.pop()

        backtrack(0)

        return res
        
            
        