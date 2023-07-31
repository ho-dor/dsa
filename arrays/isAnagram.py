class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ma = {}
        # add for first string
        for c in s:
            if c in ma:
                ma[c] = ma.get(c)+1
            else:
                ma[c] = 1
        # checking for second string
        for c in t:
            if c not in ma:
                return False
            else:
                ma[c] = ma[c] - 1

        v = ma.values()
        for item in v:
            if item != 0:
                return False
        return True
        