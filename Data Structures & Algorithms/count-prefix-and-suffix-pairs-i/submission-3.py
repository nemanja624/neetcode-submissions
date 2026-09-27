class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        count = 0
        n = len(words)

        for i in range(n):
            for j in range(i + 1, n):
                if self.isPrefixAndSuffix(words[i], words[j]):
                    count += 1

        return count
        
    def isPrefixAndSuffix(self, str1, str2):
        if not str1 and not str2:
            return True

        if not str1 or not str2:
            return False

        if str2.startswith(str1) and str2.endswith(str1):
            return True

        return False