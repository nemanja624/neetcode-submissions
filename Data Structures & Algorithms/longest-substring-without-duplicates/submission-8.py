class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        l = 0
        longest = 0

        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
                
            charSet.add(s[r])

            longest = max(longest, r - l + 1)

        return longest
































        # desni pointer se pomera
        # dok je desni u set-u, remove left i increment
        # add right u set
        # longest = max(longest, right - left + 1)
