class Solution(object):
    def diffWaysToCompute(self, input):
        memo = {}  # 전역적으로 공유되지 않도록 매 호출마다 새롭게 생성

        def computeWays(expression):
            if expression in memo:
                return memo[expression]

            if expression.isdigit():
                return [int(expression)]

            res = []

            for index, value in enumerate(expression):
                if value in "-+*":  # 연산자일 때만 분할 연산 수행
                    left = computeWays(expression[:index])
                    right = computeWays(expression[index + 1:])

                    for l in left:
                        for r in right:
                            if value == '+':
                                res.append(l + r)
                            elif value == '-':
                                res.append(l - r)
                            elif value == '*':
                                res.append(l * r)

            memo[expression] = res
            return res

        return computeWays(input)