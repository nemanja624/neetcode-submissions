class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(char.lower() for char in s if char.isalnum())
        halfway = len(s) // 2
        first_part = []
        second_part = []

        for i in range(halfway):
            first_part.append(s[i])

        for i in range(len(s) - 1, len(s) - 1 - halfway, - 1):
            second_part.append(s[i])

        if first_part == second_part:
            return True
        else:
            return False
