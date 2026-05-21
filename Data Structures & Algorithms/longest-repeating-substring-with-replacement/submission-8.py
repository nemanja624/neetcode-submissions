class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        my_dict = {}
        left = 0
        longest = 0
        max_freq = 0

        for right in range(len(s)):
            if s[right] in my_dict:
                my_dict[s[right]] += 1
            else:
                my_dict[s[right]] = 1

            max_freq = max(max_freq, my_dict[s[right]])

            while (right - left + 1) - max_freq > k:
                my_dict[s[left]] -= 1
                left += 1

            longest = max(longest, right - left + 1)

        return longest


            

            


            



















        # recnik pamti right koji se pomera
        # nadji max_frequency 
        # while prozor - max_freq > k:
        # pomeri left unapred, i izbaci element koji nije vise u prozoru iz recnika
        # longest = max(longest, right - left + 1)
        