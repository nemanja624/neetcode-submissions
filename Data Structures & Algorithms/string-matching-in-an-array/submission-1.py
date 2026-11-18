class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        joined = " ".join(words)
        res = []

        for word in words:
            if joined.count(word) > 1:
                res.append(word)

        return res

            


