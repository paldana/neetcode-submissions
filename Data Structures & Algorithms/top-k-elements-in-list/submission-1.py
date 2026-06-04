class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == 1:
            return nums
        
        # need a counter to count the occurences of the numbers in nums
        counter = {}        # key: number, value: occurences

        for num in nums:
            counter[num] = counter.get(num, 0) + 1
        
        # reorder the hash map in descending order to retrieve the K-most frequent numbers
        sorted_counter = sorted(counter.items(), key = lambda item: item[1], reverse=True)  # returns a list of tuple

        kFreq = []
        for i in range(k):
            # to access the "key" of the (key, value) tupple, we use [0] as the 2nd index
            # i.e. [(4,3), (2,2), (1,1)] --> sorted_counter[0] = (4,3); sorted_counter[0][0] = 4
            kFreq.append(sorted_counter[i][0])

        return kFreq

        # Time: O(n*k)