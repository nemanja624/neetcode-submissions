class Solution:
    def minWindow(self, s: str, t: str) -> str:
        left = 0
        count, window = {}, {}
        res, res_len = [-1, -1], float("inf")

        for char in t:
            if char in count:
                count[char] += 1
            else:
                count[char] = 1

        have, need = 0, len(count)

        for right in range(len(s)):
            if s[right] in window:
                window[s[right]] += 1
            else:
                window[s[right]] = 1

            if s[right] in count and count[s[right]] == window[s[right]]:
                have += 1

            while have == need:
                if (right - left + 1) < res_len:
                    res = [left, right]
                    res_len = right - left + 1

                window[s[left]] -= 1

                if s[left] in count and count[s[left]] > window[s[left]]:
                    have -= 1

                left += 1

        left, right = res

        return "" if res_len == float("inf") else s[left:right+1]










