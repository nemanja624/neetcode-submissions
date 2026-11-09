class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_strs = []

        for s in strs:
            encoded_strs.append(f"{len(s)}!{s}")
        
        return "".join(encoded_strs)

    def decode(self, s: str) -> List[str]:
        res = []
        cursor = 0

        while cursor < len(s):
            jump = ""
            while s[cursor] != "!":
                jump += s[cursor]
                cursor += 1
            
            cursor += 1
            jump = int(jump)
            res.append(s[cursor:cursor + jump])
            cursor += jump

        return res
