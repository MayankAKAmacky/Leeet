class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        set_nums = set(nums)

        for n in range(len(nums)+1):
            if n not in set_nums:
                return n