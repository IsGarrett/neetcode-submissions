class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:


        
        ans = 0
        l = 0
        r = len(numbers) -1


        while l < r:
            ans = numbers[r] + numbers[l]
            if ans > target:
                r -= 1
            elif ans < target:
                l += 1
            else: 
                return [l+1, r+1]