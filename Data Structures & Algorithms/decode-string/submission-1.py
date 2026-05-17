class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        current_num = 0
        current_string = ""

        for char in s:
            if char.isdigit():
                current_num = current_num * 10 + int(char)
            elif char.isalpha():
                current_string += char
            elif char == '[':
                stack.append((current_num, current_string))
                current_num = 0
                current_string = ""
            else:
                num, prev_string = stack.pop()
                current_string = prev_string + (num * current_string)

        return current_string

        



