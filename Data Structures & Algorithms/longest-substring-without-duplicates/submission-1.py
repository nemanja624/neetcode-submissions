class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        left = 0
        my_set = set()

        for right in range(len(s)):
            while s[right] in my_set:
                my_set.remove(s[left])
                left += 1
            
            my_set.add(s[right])

            longest = max(longest, right - left + 1)

        return longest


































        # desni pointer se pomera
        # dok je desni u set-u, remove left i increment
        # add right u set
        # longest = max(longest, right - left + 1)
