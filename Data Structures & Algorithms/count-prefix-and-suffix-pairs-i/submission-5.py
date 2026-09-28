class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        n = len(words)
        count = 0

        for i in range(n):
            for j in range(i + 1, n):
                if self.isPrefixAndSuffix(words[j], words[i]):
                    count += 1

        return count


    def isPrefixAndSuffix(self, str1, str2):
        if not str1 and not str2:
            return True

        if not str1 or not str2:
            return False

        if str1.startswith(str2) and str1.endswith(str2):
            return True

        return False

        