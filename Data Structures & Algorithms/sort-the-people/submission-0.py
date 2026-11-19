class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        ph = {}
        res = []

        for i in range(len(heights)):
            ph[heights[i]] = names[i]

        sorted_ph = sorted(ph, reverse=True)

        for h in sorted_ph:
            res.append(ph[h])

        return res





        