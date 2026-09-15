## Backtracking 
# Time complexity: O(N * 3^(N/7))   
#   --> NeetBot explanation: this solution is more like O(N*log(N) + W*K)
#       - O(N*log(N)) comes from extracting and sorting the options in store_all_options
#       - O(W*K) comes from generate_words, where W is number of all words x length of each word, K
# Space Complexity: O(N)
# - where N is the lenght of string s
class Solution:
    def expand(self, s: str) -> List[str]:
        all_options = []

        # Store all options for each position - only called once
        def store_all_options():
            pos = 0
            while pos < len(s):
                curr_options = []
                # If the first character is not '{', it means a single character
                if s[pos] != '{':
                    curr_options.append(s[pos])
                else:
                    # Store all the characters between '{' and '}'
                    while s[pos] != '}':
                        if 'a' <= s[pos] <= 'z':
                            curr_options.append(s[pos])
                        pos += 1
                    # Sort the list
                    curr_options.sort()
                # i.e. s = "{a,b}c{d,e}f"
                # all_options would look like this = [['a', 'b'], ['c'], ['d', 'e'], ['f']]
                all_options.append(curr_options)    
                pos += 1

        def generate_words(curr_string, expanded_words):        # called recursively
            # If the currString is complete, we can store and return
            if len(curr_string) == len(all_options):
                expanded_words.append(''.join(curr_string))
                return

            # Fetch the options for the current index
            curr_options = all_options[len(curr_string)]

            # Add the character and go into recursion
            for c in curr_options:
                curr_string.append(c)
                generate_words(curr_string, expanded_words)
                # Backtrack to previous state
                curr_string.pop()

        # Store the character options for different indices
        store_all_options()
        expanded_words = []
        generate_words([], expanded_words)
        return expanded_words