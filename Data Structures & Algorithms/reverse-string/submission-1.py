class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left = 0
        right = len(s) - 1

        while left < right:
            temp1 = s[left]
            temp2 = s[right]
            s[left] = temp2
            s[right] = temp1
            left += 1
            right -= 1