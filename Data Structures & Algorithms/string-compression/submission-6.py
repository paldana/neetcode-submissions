## Two Pointer approach

class Solution:
    def compress(self, chars: List[str]) -> int:
        """ Algorithm
        Have 1 pointer for the chars array and another at the beginning that will start moving
        once we need to modify the list with the compressed String
        """ 
        n = len(chars)
        k, i = 0, 0
        ch = chars[0]
        counter = 0
        while i < n:
            if ch != chars[i]:
                print(k)
                chars[k] = ch
                k+=1
                if counter != 1:
                    digits = list(str(counter))
                    for d in digits:
                        chars[k] = d
                        k += 1
                
                ch = chars[i]
                counter = 1
            else:
                counter += 1
            i += 1
        
        if i == n:
            chars[k] = ch
            k+=1
            if counter != 1:
                digits = list(str(counter))
                for d in digits:
                    chars[k] = d
                    k += 1
        print(chars)
        print(k)
        return k