#Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

#1 3 17 19 300

#5 6 20 91 101


#1 3 17 27 28 29 34  37 300

#15 25 35 91 101


class Solution(object):
    @staticmethod
    def binary_search(start, end, lst, value):
        if start == end:
            return start
        if lst[(start+end)//2] < value:
            return Solution.binary_search(start, (start+end)//2, lst, value)
        elif lst[(start+end)//2] == value:
            return (start+end)//2
        else:
            return Solution.binary_search((start + end) // 2, end, lst, value)

    def findMedianSortedArrays(self, nums1, nums2, m, n):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """

        medianloc = (m + n) //2
        if nums1[m//2] < nums2[n//2]:
            k = Solution.binary_search(n//2, n, nums1, nums1[m//2])
            p = Solution.binary_search(0, m//2, nums2, nums1[k])
            if (k + p) < (m+n)//2


