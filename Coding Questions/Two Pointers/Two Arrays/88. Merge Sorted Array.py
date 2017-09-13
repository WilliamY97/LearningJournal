class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        i = m-1
        j = n-1
        k = m+n-1
        
        # while there are still values in atleast the num1 or num2 array to put into num1
        while i >= 0 and j >= 0 and k >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1
        # if there are left over values in num2 then we take them and put them at the end of our iteration
        # since they're already sorted so they fit in without any other processing
        # if there are left over values in num1 it doesnt matter because they already exist in the num1 array we are changing
        if j >= 0:
            nums1[:j+1] = nums2[:j+1]
