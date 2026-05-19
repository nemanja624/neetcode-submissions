class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        longest = 0
        charSet = set()
        

        for right in range(len(s)):
            while s[right] in charSet:
                charSet.remove(s[left])
                left += 1
    
            longest = max(longest, right - left + 1)

            charSet.add(s[right])

        return longest
































        # desni pointer se pomera
        # dok je desni u set-u, remove left i increment
        # add right u set
        # longest = max(longest, right - left + 1)
