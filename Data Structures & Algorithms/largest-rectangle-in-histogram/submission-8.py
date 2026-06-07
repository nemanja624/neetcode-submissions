class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0

        for i, h in enumerate(heights):
            start = i
            while stack and h < stack[-1][1]:
                index, height = stack.pop()
                max_area = max(max_area, height * (i - index))
                start = index

            stack.append((start, h))

        for i, h in stack:
            max_area = max(max_area, h * (len(heights) - i))

        return max_area































    
    # za svakog postavi start index

    # ako je trenutna visina manja od poslednje na steku, pop i izracunaj max

    # postavi start(pocetni index) na staru poziciju, tj kao prosirivanje

    # apenduj novi taj pocetni index i visinu trenutnog

    # prodji kroz ostale(koji nemaju manjih sa desne strane)
    # izracunaj njihov max area i returnuj max area











