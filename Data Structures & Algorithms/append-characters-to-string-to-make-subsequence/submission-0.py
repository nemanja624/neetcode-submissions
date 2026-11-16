class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        count = 0
        i = 0

        for char in s:
            if char == t[i]:
                count += 1
                i += 1

            if i == len(t):
                break

        print(i)

        return len(t) - count

