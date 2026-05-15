class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for op in tokens:
            if op in {"+", "-", "*", "/"}:
                b = stack.pop()
                a = stack.pop()
                if op == "+":
                    stack.append(a + b)
                elif op == "-":
                    stack.append(a - b)
                elif op == "*":
                    stack.append(a * b)
                else:
                    # Poseban slučaj za deljenje (trunkirano ka nuli, kao na LeetCode-u)
                    stack.append(int(a / b))
            else:
                stack.append(int(op))

        return stack[0]