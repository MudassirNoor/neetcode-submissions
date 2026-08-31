class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operands = ["+", "-", "*", "/"]
        inputs = []
        for i in tokens:
            if i in operands:
                i2 = inputs.pop()
                i1 = inputs.pop()
                if i == "+":
                    inputs.append(i1 + i2)
                elif i == "-":
                    inputs.append(i1 - i2)
                elif i == "*":
                    inputs.append(i1 * i2)
                else:
                    inputs.append(int(i1 / i2))
            else:
                inputs.append(int(i))
        
        return inputs.pop()
        
