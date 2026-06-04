class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == 1:
            return nums
        
        # need a counter to count the occurences of the numbers in nums
        counter = {}        # key: number, value: occurences

        for num in nums:
            counter[num] = counter.get(num, 0) + 1
        
        # reorder the hash map in descending order to retrieve the K-most frequent numbers
        sorted_counter = sorted(counter.items(), key = lambda item: item[1], reverse=True)

        kFreq = []
        for i in range(k):
            kFreq.append(sorted_counter[i][0])

        return kFreq