class Solution(object):
    def permute(self, nums):
        res = []
        prev = []

        def dfs(elements):
            if len(elements) == 0:
                res.append(prev[:])

            for e in elements:
                next_e = elements[:]
                next_e.remove(e)

                prev.append(e)
                dfs(next_e)
                prev.pop()

        dfs(nums)
        return res