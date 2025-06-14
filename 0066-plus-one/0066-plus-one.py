class Solution(object):
    def plusOne(self, digits):
        before = ''.join(map(str, digits))
        before_int = int(before) + 1
        before_str = str(before_int)

        return self.toList(before_str)

    def toList(self, before_str):
        res = []
        for i in before_str:
            res.append(int(i))

        return res

    
        