class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # sum = 0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                add= nums[i]+nums[j]
                if add == target:
                    return [i,j]