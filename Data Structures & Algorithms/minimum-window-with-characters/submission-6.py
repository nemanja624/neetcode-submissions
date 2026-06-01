class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        
        l, r = 0, 0
        res, res_len = [-1, -1], float("inf")
        count, window = {}, {}

        for char in t:
            if char in count:
                count[char] += 1
            else:
                count[char] = 1

        have, need = 0, len(count)

        for r in range(len(s)):
            if s[r] in window:
                window[s[r]] += 1
            else:
                window[s[r]] = 1

            if s[r] in count and count[s[r]] == window[s[r]]:
                have += 1

            while have == need:
                if (r - l + 1) < res_len:
                    res = [l, r]
                    res_len = r - l + 1
                    
                window[s[l]] -= 1

                if s[l] in count and count[s[l]] > window[s[l]]:
                    have -= 1

                l += 1

        l, r = res

        return "" if res_len == float("inf") else s[l:r+1]











