## Backtracking Approach - Personal Attempt
class Solution:
    def expand(self, s: str) -> List[str]:
        all_options = []

        #1 - extract all options from s and put them in an array
        i = 0
        while i < len(s):
            if s[i] != '{':
                all_options.append(s[i])
            else:
                curr_options = []   # temp array to store all the options within the {}
                while s[i] != '}':
                    # get all characters from the options between {}
                    if 'a' <= s[i] <= 'z':
                        curr_options.append(s[i])
                    i += 1
                curr_options.sort()
                all_options.append(curr_options)
            
            i += 1      # keep going through the whole s string
        
        #2 - at this point, we can start constructing words piece by piece
        # create a helper function that will be used to recursively create the expanded words
        def generate_words(currWord, expandedWords):
            # base case - if current word matches the number of available options - add to the output list
            if len(currWord) == len(all_options):
                expandedWords.append("".join(currWord))     # since currWord will look like this - ["a","b","c"], join them to form a single string
                return

            # get the current available option from the list using the len of currWord as the index
            curr_options = all_options[len(currWord)]

            for c in curr_options:
                currWord.append(c)
                # run this function recursively to build the string
                generate_words(currWord, expandedWords)

                # backtrack by removing the just added option to create a new word
                currWord.pop()
            
            return 

            
        expandedWords = []
        generate_words([], expandedWords)
        return expandedWords



        
                
