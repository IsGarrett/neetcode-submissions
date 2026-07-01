class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        

        l = 0
        r = 1

        myMap = {}


        for i in range(len(nums)):

            complement = target - nums[i]
            if complement in myMap:
                return [myMap[complement], i]
            else:
                myMap[nums[i]] = i
        return [0, 0]


            