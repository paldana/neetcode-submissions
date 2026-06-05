class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)

        sortedNums = sorted(nums)
        streak = 1
        longestStreak = 0
        
        prevVal = sortedNums[0]
        for n in sortedNums:
            if prevVal+1 == n:
                 streak += 1
            elif prevVal == n:
                pass
            else: 
                streak = 1
            prevVal = n
            longestStreak = max(longestStreak, streak)
        
        return longestStreak
