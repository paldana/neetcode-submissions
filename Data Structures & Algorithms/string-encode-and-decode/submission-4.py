class Solution:

    def encode(self, strs: List[str]) -> str:
        enc_str = []
        enc_str.append("!"+"-")
        
        for s in strs:
            s_len = len(s)
            enc_str.append("#"+str(s_len)+"-"+s+"-")
    
        enc_str.append("!")
        return "".join(enc_str)


    def decode(self, s: str) -> List[str]:
        split_s = s.split("-")
        tkn_size = 0
        dec_str = []
        data = False
        for token in split_s:
            if data and tkn_size == len(token):
                dec_str.append(token)
                data = False
            elif "#" in token:
                tkn_size = int(token[1:])
                data = True

        return dec_str
                