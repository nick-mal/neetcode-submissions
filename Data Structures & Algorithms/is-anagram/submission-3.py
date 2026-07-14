from collections import defaultdict
 
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        n = len(s)
        s_cnts = defaultdict(int)
        t_cnts = defaultdict(int)

        for i in range(len(s)):
            s_cnts[s[i]] += 1
            t_cnts[t[i]] += 1

        return s_cnts == t_cnts
        