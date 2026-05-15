class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for op in tokens:
            if op in {'+', '-', '*', '/'}:
                b = stack.pop()
                a = stack.pop()
                if op == '+':
                    result = a + b
                    stack.append(result)
                elif op == '-':
                    result = a - b
                    stack.append(result)
                elif op == '*':
                    result = a * b
                    stack.append(result)
                else:
                    result = a / b
                    stack.append(int(result))
            else:
                stack.append(int(op))

        return stack[0]
                