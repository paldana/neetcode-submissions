## Greedy Solution 
# Time: O(n), Space: O(26) - hashmap of chars
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastIndexMap = {}   # key: char, value: last index of char in string s
        for i, char in enumerate(s):
            lastIndexMap[char] = i      # extract last index of each character
                                        # by going through the list in one pass
        
        """
        Go through the string again and keep track of two counters, size and partEnd.  
        Size will be the partition size which will be appended to res. 
        Partition end, partEnd, will be used to keep track of the farthest 
        index of one of the characters in the partition.

        As we go through the current partition, we update partEnd if the current
        partEnd is less than the last index of the current character. 
        Once the current index reaches partEnd, then we've found a partition
        and we save the current size and reset to 0 to look for the next part.
        """
        res = []
        size, partEnd = 0, 0
        for i, char in enumerate(s):
            size += 1
            partEnd = max(partEnd, lastIndexMap[char]) # 

            if i == partEnd:
                res.append(size)
                size = 0
        return res