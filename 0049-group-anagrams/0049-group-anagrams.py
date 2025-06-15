class Solution(object):
    def groupAnagrams(self, strs):
        import collections as c

        res = c.defaultdict(list)

        for s in strs:
            res[''.join(sorted(s))].append(s)

        return list(res.values())


