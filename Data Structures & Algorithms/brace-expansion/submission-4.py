## Iteration Solution
# Time complexity: O(N * 3^(N/7))
# Space Complexity: O(N * 3^(N/7))
# - where N is the lenght of string s
class Solution:
    def expand(self, s: str) -> List[str]:
        def storeFirstOptions(startPos, firstOptions):
            # If the first character is not '{', it means a single character
            if s[startPos] != '{':
                firstOptions.append(s[startPos])
            else:
                # Store all the characters between '{' and '}'
                while s[startPos] != '}':
                    if 'a' <= s[startPos] <= 'z':
                        firstOptions.append(s[startPos])
                    startPos += 1
                # Sort the list
                firstOptions.sort()
            # Increment it to point to the next character to be considered
            return startPos + 1

        expandedWords = [""]
        startPos = 0
        while startPos < len(s):
            firstOptions = []
            # Store the characters for the first index as string in firstOptions
            remStringStartPos = storeFirstOptions(startPos, firstOptions)

            currWords = []
            # Append the string in the list firstOptions to string in expandedWords
            for word in expandedWords:
                for c in firstOptions:
                    currWords.append(word + c)

            # Update the list expandedWords to have all the words
            expandedWords = currWords
            # Pointing to the next character to be considered
            startPos = remStringStartPos

        return expandedWords