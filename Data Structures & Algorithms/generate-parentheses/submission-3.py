class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 0:
            return []
        
        res = []

        def backtrack(opnd: int, clsd: int, s: str):
            if len(s) == 2 * n:
                res.append(s)
                return

            if opnd < n:
                backtrack(opnd + 1, clsd, s + "(")

            if clsd < opnd:
                backtrack(opnd, clsd + 1, s + ")")

        backtrack(0, 0, "")

        return res

