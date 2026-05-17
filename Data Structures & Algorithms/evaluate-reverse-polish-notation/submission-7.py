class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        res = 0

        for op in tokens:
            if op in {'+', '-', '*', '/'}:
                b = stack.pop()
                a = stack.pop()
                if op == '+':
                    res = a + b
                    stack.append(res)
                elif op == '-':
                    res = a - b
                    stack.append(res)
                elif op == '*':
                    res = a * b
                    stack.append(res)
                else:
                    res = a / b
                    stack.append(int(res))
            else:
                stack.append(int(op))
            
        return stack[0]