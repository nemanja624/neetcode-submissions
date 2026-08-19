class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack = []

        for op in logs:
            if op == "../":
                if len(stack) != 0:
                    stack.pop()
                else:
                    continue

            elif op == "./":
                continue
            
            else:
                stack.append(op)

        return len(stack)