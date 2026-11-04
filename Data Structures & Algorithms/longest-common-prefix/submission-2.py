class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]

        for s in strs:
            if prefix == "":
                return ""

            while not s.startswith(prefix):
                prefix = prefix[:-1]

        return prefix



      

