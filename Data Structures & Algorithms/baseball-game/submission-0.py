class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []

        for op in operations:
            if op == '+':
                if not stack:
                    return False
                else:
                    stack.append(stack[-1] + stack[-2])

            elif op == 'C':
                if not stack:
                    return False
                else:
                    stack.pop()

            elif op == 'D':
                if not stack:
                    return False
                else:
                    stack.append(stack[-1] * 2)
            
            else:
                stack.append(int(op))

        return sum(stack)
                   
