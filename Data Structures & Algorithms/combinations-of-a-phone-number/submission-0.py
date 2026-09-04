class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        digitCharMap = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz"
        }

        def backtrack(i, currString):
            # base case
            if i == len(digits):
                res.append(currString)
                return

            chars = digitCharMap[digits[i]]
            for c in chars:
                backtrack(i+1, currString + c)
            
            return
        if digits:
            backtrack(0, "")
        return res