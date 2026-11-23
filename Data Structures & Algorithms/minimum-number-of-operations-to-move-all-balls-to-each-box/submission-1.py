class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        res = [0] * n
        balls = 0
        ops = 0

        for i in range(len(boxes)):
            ops += balls

            res[i] = ops

            if boxes[i] == "1":
                balls += 1

        ops = 0
        balls = 0

        for j in range(len(boxes) - 1, - 1, - 1):
            ops += balls

            res[j] += ops

            if boxes[j] == "1":
                balls += 1

        return res
