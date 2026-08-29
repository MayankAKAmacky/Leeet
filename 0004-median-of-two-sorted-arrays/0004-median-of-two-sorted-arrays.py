class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        final_num = []
        i, j = 0,0
        m = len(nums1)
        n = len(nums2)

        while i<m and j<n:
            if nums1[i] <= nums2[j]:
                final_num.append(nums1[i])
                i+=1
            else:
                final_num.append(nums2[j])
                j+=1

        final_num.extend(nums1[i:])
        final_num.extend(nums2[j:])

        
        mid = len(final_num) // 2
        if len(final_num) % 2 == 0:
            return (final_num[mid -1] + final_num[mid]) / 2.0
        else:
            return final_num[mid]