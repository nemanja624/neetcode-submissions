class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        left = 0
        k = len(s1)
        count1 = [0] * 26
        count2 = [0] * 26

        for char in s1:
            count1[ord(char) - ord('a')] += 1

        for char in s2[:k]:
            count2[ord(char) - ord('a')] += 1

        if count1 == count2:
            return True

        for i in range(k, len(s2)):
            count2[ord(s2[i]) - ord('a')] += 1
            count2[ord(s2[i - k]) - ord('a')] -= 1

            if count1 == count2:
                return True
        
        return False


        





