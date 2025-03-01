class Solution(object):
    def diffWaysToCompute(self, input):
        
        def compute(left, right, op):
            res = []

            for l in left:
                for r in right:
                    res.append(eval(str(l) + op + str(r)))
            return res
        
        if input.isdigit():
            return [int(input)]

        res = []

        for index, value in enumerate(input):
            if value in "-+*":
                left = self.diffWaysToCompute(input[:index])
                right = self.diffWaysToCompute(input[index + 1:])

                res.extend(compute(left, right, value))
        
        return res