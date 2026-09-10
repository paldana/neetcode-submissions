class Solution:
    def compress(self, chars: List[str]) -> int:
        n = len(chars)

        ch, counter = chars[0], 0
        i = 0
        while i < n:
            if ch != chars[i]:
                chars.append(ch)

                if counter != 1:
                 # converts counter into string then split the string individually in an array
                 # i.e. counter = 11 -> str(counter) -> "11" -> list(str(counter)) -> ["1", "1"]
                    chars += list(str(counter))     # add the converted counter list to the existing chars list

                # alternatively, convert counter manually...

                # reset ch and counter to start with the new sequence of characters
                ch = chars[i]
                counter = 1
            else:
                counter += 1
            
            i += 1
        
        # if we've reached end of original chars list, append the remaining values to chars
        if i == n:
            chars.append(ch)
            if counter != 1:
                chars += list(str(counter))

        # get the length of the compressed string - starting from end of original chars list at n to the end of the list
        # compressedString = chars[n:]
        k = len(chars) - n

        # lastly, modify the first k elements in chars list
        for idx in range(k):
            # chars[idx] = compressedString[idx]
            chars[idx] = chars[n+idx]
        
        
        return k
