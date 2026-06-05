class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        enc_str = ""
        for s in strs:
            enc_str += str(len(s)) + "#" + s
        
        # i.e. strs=["Hello","World"]
        # enc_str = "5#Hello5#World"
        return enc_str

    def decode(self, s: str) -> List[str]:
        if not s:
            return []

        dec_str = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
        
            length = int(s[i:j]) # get the size of the original word before the '#'
            print(f"length: {length}")
            print(f"i: {i}; j: {j}")
            
            i = j + 1          # update pointer after '#'
            j = i + length     # j positioned at the end of the whole word to be extracted
            dec_str.append(s[i:i+length]) # extract the word
            i = j              # update i where j currently is and loop
        return dec_str
        
