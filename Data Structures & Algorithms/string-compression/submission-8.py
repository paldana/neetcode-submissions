## 2-pointer solution
class Solution:
    def compress(self, chars: List[str]) -> int:
        n = len(chars)
        i = k = 0

        while i < n:
            chars[k] = chars[i]
            k += 1

            # create another pointer that will scan for subsequent duplicate chars
            j = i + 1
            while j < n and chars[j] == chars[i]:
                j += 1

            # once a new char is seen, check the length of the previously seen character
            if j - i > 1:
                for c in str(j - i):    # convert the difference to string to be added to the compressed string
                    chars[k] = c
                    k += 1

            i = j  # update i to where j currently is

        return k
