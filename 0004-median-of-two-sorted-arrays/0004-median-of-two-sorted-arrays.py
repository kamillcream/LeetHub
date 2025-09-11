class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        nums3 = sorted(nums1 + nums2)
        mid_idx1 = len(nums3) // 2
        if (len(nums3) % 2 == 0):
            mid_idx2 = len(nums3) // 2 - 1 
            return (nums3[mid_idx1] + nums3[mid_idx2]) / 2.0
        
        return nums3[mid_idx1]
       
        