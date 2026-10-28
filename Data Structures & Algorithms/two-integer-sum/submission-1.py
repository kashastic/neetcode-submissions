class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i,num in enumerate(nums):
            new_target=target-num
            if new_target in seen:
                return [seen[new_target],i]
            seen[num]=i
        return []

        #hashMaps
            
        