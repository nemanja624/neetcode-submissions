class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        letterMap = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        res = []
        path = []

        def backtrack(i, j):
            if i == len(digits):
                res.append("".join(path))
                return

            letters = letterMap[digits[i]]

            if j >= len(letters):
                return

            path.append(letters[j])
            backtrack(i + 1, 0)
            path.pop()
            backtrack(i, j + 1)

        backtrack(0, 0)

        return res


        