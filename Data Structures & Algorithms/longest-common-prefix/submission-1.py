class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        length = len(strs[0])
        prefix = strs[0]

        for s in strs[1:]:
            if prefix == "":
                return ""

            while not s.startswith(prefix):
                prefix = prefix[:-1]

        return prefix



      

