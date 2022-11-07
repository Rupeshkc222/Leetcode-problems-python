class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merge=sorted(nums1+nums2)
        l=len(merge)
        if l%2==0:
            return(sum(merge[(l//2)-1:(l//2)+1])/2)
        return(merge[l//2])

        '''
        Input: nums1 = [1,3], nums2 = [2]
        Output: 2.00000
        Explanation: merged array = [1,2,3] and median is 2.
        '''