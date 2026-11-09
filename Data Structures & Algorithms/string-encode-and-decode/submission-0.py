class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""

        for s in strs:
            size = len(s)
            res += chr(size) + s

        return res        

    def decode(self, s: str) -> List[str]:
        res = []

        while s:
            size = ord(s[0])
            word = s[1:size + 1]
            res.append(word)
            s = s[size + 1:]

        return res




