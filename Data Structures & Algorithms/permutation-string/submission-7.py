class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        k = len(s1)
        l = 0
        r = 0

        count1 = [0] * 26
        count2 = [0] * 26

        for char in s1:
            count1[ord(char) - ord('a')] += 1

        for char in s2[:k]:
            count2[ord(char) - ord('a')] += 1

        if count1 == count2:
            return True

        for r in range(k, len(s2)):
            count2[ord(s2[r]) - ord('a')] += 1
            count2[ord(s2[r - k]) - ord('a')] -= 1

            if count1 == count2:
                return True

        return False




        





