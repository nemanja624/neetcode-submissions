class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {")": "(", "]": "[", "}": "{"}
        stack = []

        for b in s:
            if b in brackets:
                if not stack:
                    return False
                top_element = stack.pop()
                if top_element != brackets[b]:
                    return False
            else:
                stack.append(b)

        return not stack
