class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []

        for i, t in enumerate(temperatures):
            while stack and t > temperatures[stack[-1]]:
                popped_index = stack.pop()
                result[popped_index] = i - popped_index
            stack.append(i)

        return result

                
   