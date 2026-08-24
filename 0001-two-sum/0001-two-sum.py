class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        seen = {}

        for n , num in enumerate(nums):
            needed = target - num

            if target - num in seen: 
                return [seen[needed], n]
            seen[num]= n
            