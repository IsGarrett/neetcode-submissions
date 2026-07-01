class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        

        left = 0
        right = len(numbers)-1

        while left <= right:

            total = numbers[left] + numbers[right]
            print(total)
            if total == target:
                return [left+1, right+1]
            if total < target:
                print(left)
                left +=1
            else:
                right -=1
        return []
