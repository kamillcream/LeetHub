from collections import Counter

class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        r = Counter(ransomNote)
        m = Counter(magazine)
        return all(r[c] <= m[c] for c in r)