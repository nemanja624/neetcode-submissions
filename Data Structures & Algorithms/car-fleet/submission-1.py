class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = [[p, s] for p, s in zip(position, speed)]
        cars.sort(reverse=True)
        stack = []

        for p, s in cars:
            time = (target - p) / s
            if not stack or time > stack[-1]:
                stack.append(time)

        return len(stack)











    # parovi position, speed

    # vreme

    # ako ga stize, nemoj ga apendovati

    # vrati duzinu steka














        #HINT
        # sort od najblizeg ka najdaljem
        # parovi position, speed
        # time = (target - position) / speed
        # ako je time veci ili je stek prazan, apenduj
        # vrati length

