class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        

        stack = []
        cars = list(zip(position, speed))
        cars.sort(reverse=True)
        
        

        for pos, spd in cars:
            arrive = (target - pos) / spd
            if not stack or arrive > stack[-1]:
                stack.append(arrive)
        
        return (len(stack))
