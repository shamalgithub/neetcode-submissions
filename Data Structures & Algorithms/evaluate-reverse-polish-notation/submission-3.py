# fully solved alone !!!! 

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = {"+", "-", "*", "/"}
        numbers_stack = []

        for t in tokens:
            if t in operators:
                b = numbers_stack.pop()  # second operand (pushed last)
                a = numbers_stack.pop()  # first operand (pushed first)

                if t == "+":
                    result = a + b
                elif t == "-":
                    result = a - b
                elif t == "*":
                    result = a * b
                elif t == "/":
                    result = int(a / b)  # truncate toward zero

                numbers_stack.append(result)
            else:
                numbers_stack.append(int(t))

        return numbers_stack[0]



        