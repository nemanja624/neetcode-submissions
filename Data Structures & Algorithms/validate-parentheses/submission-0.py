class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {}
        stack = []

        brackets[')'] = '('
        brackets[']'] = '['
        brackets['}'] = '{'

        for bracket in s:
            if bracket == '{' or bracket == "(" or bracket == '[':
                stack.append(bracket)
            elif bracket == '}' or bracket == ')' or bracket == ']':
                if not stack:
                    return False
                else:
                    open_bracket = stack.pop()
                    if open_bracket != brackets[bracket]:
                        return False

        return not stack
                





        
        