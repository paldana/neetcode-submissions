class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        total = len(nums1) + len(nums2)
        half = total // 2

        # We would want A to be the shorter list
        if len(B) < len(A):
            A, B = B, A

        # Perform binary search on shorter list (A) to get the midpoint for B
        l, r = 0, len(A) - 1
        while True:
            i = (l + r) // 2    # i pointer is for A's midpoint
            j = half - i - 2    # j pointer is for B's midpoint; 
                                # the -2 is because the i and j ptrs are 0-indexed
                                # ==> j = half - (i + 1) - 1
                                # so total elements on the left of both arrays equals "half"

            # Get the boundaries of the left and right partitions using the i and j pointers
            Aleft = A[i] if i >= 0 else float("-infinity")
            Aright = A[i + 1] if (i + 1) < len(A) else float("infinity")
            Bleft = B[j] if j >= 0 else float("-infinity")
            Bright = B[j + 1] if (j + 1) < len(B) else float("infinity")

            ## Check if partitions are correctly set
            # Correct partition selected
            if Aleft <= Bright and Bleft <= Aright:
                # check if there are odd number of combined elements
                if total % 2:   
                    return min(Aright, Bright)  # return median
                else:
                    # if even, add 2 medians / 2
                    return (max(Aleft, Bleft) + min(Aright, Bright)) / 2   
            # if not move the l and r pointers to get the correct partitions        
            elif Aleft > Bright:
                r = i - 1
            else:
                l = i + 1