class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        l = 0
        longest = 0
        max_freq = 0

        for r in range(len(s)):
            if s[r] in count:
                count[s[r]] += 1
            else:
                count[s[r]] = 1

            max_freq = max(max_freq, count[s[r]])

            while (r - l + 1) - max_freq > k:
                count[s[l]] -= 1
                l += 1

            longest = max(longest, r - l + 1)

        return longest

 






            

            


            



















        # recnik pamti right koji se pomera
        # nadji max_frequency 
        # while prozor - max_freq > k:
        # pomeri left unapred, i izbaci element koji nije vise u prozoru iz recnika
        # longest = max(longest, right - left + 1)
        