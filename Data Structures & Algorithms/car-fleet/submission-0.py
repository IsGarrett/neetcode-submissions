class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        

        stack = []
        cars = list(zip(position, speed))
        cars.sort(reverse=True)
        arrive = (target - cars[0][0]) / cars[0][1]
        stack.append(arrive)
        

        for car in cars:
            arrive = (target - car[0]) / car[1]
            if arrive > stack[-1]:
                stack.append(arrive)
        
        return (len(stack))
