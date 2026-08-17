class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ### Brute Force Solution ###
        ## Time: O(k*(n-k)) ; Space: O(n)
        # res = []
        # for i in range(len(nums) - k + 1):
        #     maxNum = nums[i]
        #     for j in range(i, i + k):
        #         maxNum = max(maxNum, nums[j])
        #     res.append(maxNum)
        # return res


        ### Deque Solution ###
        ## Time and Space: O(n)
        output = []
        q = deque()  # index of num values from nums list
        l = r = 0    # represents the window

        while r < len(nums):
            # pop smaller values from q
            while q and nums[q[-1]] < nums[r]:
                q.pop()     # pop from the top/rightmost of queue (recently added)
            q.append(r)

            # remove leftmost index from the queue if left pointer, l, increased 
            # (sliding window moved, now the left index in q is out of bounds)
            # -- this effectively remove the values from the window
            if l > q[0]:
                q.popleft()

            # if current window is at least size k -- +1 cause 0-indexed
            if (r + 1) >= k:
                output.append(nums[q[0]])       # max val of the window is the leftmost index in q
                l += 1      # only incremented if we already have a k-window

            r += 1

        return output