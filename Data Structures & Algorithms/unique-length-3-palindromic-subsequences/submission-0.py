class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        first = [-1] * 26
        last = [-1] * 26

        count = 0

        for i, char in enumerate(s):
            idx = ord(char) - ord('a')

            if first[idx] == -1:
                first[idx] = i

            last[idx] = i

        for c in range(26):
            if first[c] == -1 or first[c] == last[c]:
                continue

            part = s[first[c] + 1 : last[c]]

            count += len(set(part))

        return count