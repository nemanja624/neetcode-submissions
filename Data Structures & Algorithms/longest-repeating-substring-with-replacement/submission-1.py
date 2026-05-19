class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        my_dict = {}
        longest = 0
        max_f = 0
        
        for right in range(len(s)):
            if s[right] in my_dict:
                my_dict[s[right]] += 1
            else:
                my_dict[s[right]] = 1

            max_f = max(max_f, my_dict[s[right]])

            while (right - left + 1) - max_f > k:
                my_dict[s[left]] -= 1
                left += 1

            longest = max(longest, right - left + 1)

        return longest