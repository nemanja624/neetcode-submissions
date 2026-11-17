class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        lastWord = ""
        res = ""

        for char in s:
            lastWord += char
            res += char

            if char == " ":
                lastWord = ""

            if len(lastWord) > 0:
                res = lastWord

        print(res)

        res = res.strip()

        return len(res) 