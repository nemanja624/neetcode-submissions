class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtrack(open_brackets: int, closed_brackets: int, s: str):
            if len(s) == 2 * n:
                res.append(s)
                return

            if open_brackets < n:
                backtrack(open_brackets + 1, closed_brackets, s + "(")

            if closed_brackets < open_brackets:
                backtrack(open_brackets, closed_brackets + 1, s + ")")

        backtrack(0, 0, "")

        return res