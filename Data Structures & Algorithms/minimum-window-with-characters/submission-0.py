class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
            
        countT = {}
        window = {}
        left = 0
        res = [-1, -1]
        res_len = float("infinity")

        for c in t:
            if c in countT:
                countT[c] += 1
            else:
                countT[c] = 1

        have = 0
        need = len(countT)

        for right in range(len(s)):
            c = s[right]
            if c in window:
                window[c] += 1
            else:
                window[c] = 1
            
            if c in countT and window[c] == countT[c]:
                have += 1
            
            while have == need:
                if (right - left + 1) < res_len:
                    res = [left, right]
                    res_len = (right - left + 1)
                
                window[s[left]] -= 1

                if s[left] in countT and window[s[left]] < countT[s[left]]:
                    have -= 1

                left += 1

        left, right = res

        return s[left:right+1] if res_len != float("infinity") else ""










