class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) == 1:
            return True

        # clean input string of spaces and non-alphanumeric characters and convert to all lowercase
        cleaned_str = "".join(char for char in s if char.isalnum()).lower()
        
         # two pointers
        i = 0
        j = len(cleaned_str) - 1    # 0-indexed array

        while i < j:
            if cleaned_str[i] == cleaned_str[j]:
                i += 1
                j -= 1
            else: 
                return False
        return True

