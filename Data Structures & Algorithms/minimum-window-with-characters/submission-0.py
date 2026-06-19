class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        countT, window = {}, {}         # 2 hash maps for countT (need), window (have)
        for c in t:
            countT[c] = 1 + countT.get(c, 0)    # initialize the hash map with the char count

        have, need = 0, len(countT)     # have is a counter to check if we've seen x chars from t in the window
        res, resLen = [-1, -1], float("infinity")   # res: indexes of [l,r] pointers; resLen: length of res window
        l = 0
        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)

            if c in countT and window[c] == countT[c]:
                have += 1

            # go through a while-loop to check if the window size can be smaller as we go through the whole string s
            while have == need:
                # if the current size of r-l pointer (+1 since 0-indexed) is smaller than the current resLen
                if (r - l + 1) < resLen:
                    # update the res and resLen to get the smaller window
                    res = [l, r]
                    resLen = r - l + 1

                # pop characters from the left by increasing l by 1
                window[s[l]] -= 1         # decrease char count from window hash
                # if the current char is in the need and 
                # we have less than the count we need to satisfy the condition 
                if s[l] in countT and window[s[l]] < countT[s[l]]:  
                    have -= 1       # decrease have counter to get out of the while-loop and proceed with the for-loop
                l += 1

        l, r = res          # res will contain the min window substring

        return s[l : r + 1] if resLen != float("infinity") else ""

# Sliding Window Solution
# Time Complexity: O(n)
# Space Complexity: O(m)
#    -- Where n is the length of the string s and m is the total number of unique
#       characters in the strings t and s.