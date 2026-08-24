class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        temp = sorted(nums)

        seen={}

        for i,num in enumerate(temp):
            if num not in seen:
                seen[num] = i

        ret=[]
        for i in nums:
            ret.append(seen[i])
        return ret
