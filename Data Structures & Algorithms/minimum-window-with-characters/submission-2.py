from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        nS, nT = len(s), len(t)
        if nT > nS:
            return ""

        # hashmap character counters for what we need, countT, and what the window has
        countT, window = Counter(t), {}
        have, need = 0, len(countT)         # need = number of character occurences that need to be satisfied
        res, resLen = [-1, -1], float("infinity")  # res = [r, l]

        l = 0
        for r in range(nS):
            ch = s[r]
            window[ch] = window.get(ch, 0) + 1

            if ch in countT and window[ch] == countT[ch]:
                have += 1

            while have == need:
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = r - l + 1

                # pop chars from left
                window[s[l]] -= 1

                if s[l] in countT and countT[s[l]] > window[s[l]]:
                    have -= 1
 
                l += 1

        l, r = res

        return s[l : r + 1] if resLen != float("infinity") else ""
