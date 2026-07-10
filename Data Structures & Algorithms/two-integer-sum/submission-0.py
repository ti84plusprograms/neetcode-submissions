class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        indices = {}
        for i, num in enumerate(nums):
            if num in indices:
                return [indices[num], i]
            
            indices[target - num] = i 
        
        return [-1, -1]