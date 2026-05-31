class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for a in asteroids:
            while stack and a < 0 and stack[-1] > 0:
                diff = a + stack[-1]

                if diff > 0:
                    a = 0
                
                elif diff < 0:
                    stack.pop()
                    continue
                    
                else:
                    stack.pop()
                    a = 0

            if a != 0:
                stack.append(a)

        return stack
                


        





























            # HINT
            # ako a nije nula, appenduj ga
            # diff = a + stack[-1]
            # provera manji veci jednako 
            
