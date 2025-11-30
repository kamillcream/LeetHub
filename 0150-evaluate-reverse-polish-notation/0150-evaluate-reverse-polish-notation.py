class Solution(object):
    def evalRPN(self, tokens):
        ops = ["+", "-", "/", "*"]
        num_stack = []
        answer = 0
        num1 = 0
        num2 = 0


        for i in tokens:
            if i not in ops:
                num_stack.append(int(i))

            if i in ops:
                num2 = num_stack.pop()
                num1 = num_stack.pop()
                answer = self.calculate(i, num1, num2)
                num_stack.append(answer)

        return num_stack.pop()
                
                

    def calculate(self, op, num1, num2):
        if op == "+":
            return num1 + num2
        elif op == "-":
            return num1 - num2
        elif op == "*":
            return num1 * num2
        elif op == "/":
            return int(float(num1) / num2)

        

            
        