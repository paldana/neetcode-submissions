class Solution:
    def compress(self, chars: List[str]) -> int:
        n = len(chars)
        # i will be the reader pointer, k will be the write pointer
        i, k = 0, 0

        while i < n:
            chars[k] = chars[i]
            k += 1
            j = i + 1  # temp pointer that will be used to check for consecutive chars
            while j < n and chars[i] == chars[j]:
                j += 1  # keep incrementing until we get a different char

            # if char count is more than 1, append it to compressed string
            if (j - i) > 1:
                for c in str(j - i):
                    chars[k] = c
                    k += 1
            
            i = j   # update i to start where j is

        return k
