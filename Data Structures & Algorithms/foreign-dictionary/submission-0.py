## DFS Solution
# Time Complexity: O(N + V + E)
# Space Complexity: O(V + E)
# -- where V is the number of unique characters, E is the number of edges, and N is the sumn of lengths of all the strings

class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        ## adjacency list as dictionary where keys are letters and values are set of adjacent letters 
        # i.e. words = ["hrn","hrf","er","enn","rfnn"]
        # adj = {'h': set(), 'r': set(), 'n': set(), 'f': set(), 'e': set()}
        adj = {c: set() for w in words for c in w}

        ## nested loop to extract the adjacent letters
        # loop will make use of 2 words at a time to compare if the conditions are met
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            minLen = min(len(w1), len(w2))      # get the len of smaller word for the prefix in the if-statement below
            
            # compare two words if it meets the condition: "a is a prefix of b and a.length < b.length.""
            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
                return ""               # return empty string if this condition is not met = words are not sorted lexicographically, hence claim is incorrect
            
            # go through each letters in the word and get the first characters that do not match
            for j in range(minLen):
                if w1[j] != w2[j]:
                    # if they don't match, add the character w2[j] to w1[j]'s adjacent list 
                    # -> the set contains all the letters that the key letter (w1[j]) is smaller to lexicographically
                    adj[w1[j]].add(w2[j])
                    break

        visited = {}    # key = character; value = boolean -> False if only visited, True if visited and in current path; if not yet in the dict, that means we haven't visited the char yet
        res = []

        ## Post Order Traversal - the res will contain the answer in reverse order
        def dfs(char):

            if char in visited:
                return visited[char]        # if we got here, that means a loop is detected, hence claim is incorrect again, so we'll return ""

            visited[char] = True            # set to True since it is visited and currently in the path for the for-loop below

            for neighChar in adj[char]:     # go through all the adjacent characters and perform DFS
                if dfs(neighChar):          # if dfs returns true, it detected a loop, so again return ""
                    return True

            visited[char] = False           # char no longer in the path after the for-loop, so set to False
            res.append(char)                # no loop detected and end of DFS, append character to res

        ## Main for-loop - go through each extracted char in the adjacency list
        for char in adj: 
            if dfs(char):
                return ""

        res.reverse()           # reverse the char list to get the correct order
        return "".join(res)     # join all the chars in the res list to form a single string as the expected output answer