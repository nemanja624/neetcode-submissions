class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = set()
        l = 0
        r = 0
        longest = 0

        for r in range(len(s)):
            while s[r] in window:
                window.remove(s[l])
                l += 1

            window.add(s[r])

            longest = max(longest, r - l + 1)

        return longest


































        # desni pointer se pomera
        # dok je desni u set-u, remove left i increment
        # add right u set
        # longest = max(longest, right - left + 1)
