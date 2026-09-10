class Solution:
    def expand(self, s: str) -> List[str]:
        ## Iterative approach - we'll create the string as we go through every options in string, s
        # Time and Space: O(n*m) - where n = len(s), m = maximum number of options in any brace group multiplied across all groups (i.e., the size of the final output list)
        # 1 - create an array to store expanding words - will be the output
        expandedWords = [""]        # need to have an empty string so we can iterate through it 
        i = 0   
        # go through every character of s
        while i < len(s):
            # create temp array that will store the new words we'll create
            options = []

            # extract the options we have from the s starting from i
            if s[i] != "{":
                options.append(s[i])
            else:
                while s[i] != "}":
                    # check if character
                    if 'a' <= s[i] <= 'z':
                        options.append(s[i])
                    i += 1
                options.sort()
                # at this point, i is pointing to an '}'

            i += 1          # increment to point to the next unvisited option in s
            newWords = []
            for word in expandedWords:
                for c in options:
                    newWords.append(word + c)
            
            # update the expandedWords to contain the newWords with the newly appended characters from options
            expandedWords = newWords
        
        return expandedWords


