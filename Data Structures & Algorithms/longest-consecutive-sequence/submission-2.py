class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest =0
        for n in nums:
            if(n-1) not in nums:
                length = 0
                while(n+length) in numSet:
                    length +=1
                longest = max(length,longest)
        return longest




        # count = 0
        # for i in range(len(nums)):
        #     if target in nums:
        #         return target
        #         count +=target
        #         target ++
