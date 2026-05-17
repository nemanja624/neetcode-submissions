class Solution:
    def decodeString(self, s: str) -> str:
        stack = [] 
        curr_num = 0
        curr_str = ""

        for char in s:
            if char.isdigit():
                curr_num = curr_num * 10 + int(char)
            elif char.isalpha():
                curr_str += char
            elif char == '[':
                stack.append((curr_num, curr_str))
                curr_num = 0
                curr_str = ""
            else:
                num, prev_str = stack.pop()
                curr_str = prev_str + (num * curr_str)

        return curr_str

