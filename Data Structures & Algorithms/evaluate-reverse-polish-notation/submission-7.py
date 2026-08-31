class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        inputs = []
        for i in tokens:
            if i == "+":
                i2, i1 = inputs.pop(), inputs.pop()
                inputs.append(i1 + i2)
            elif i == "-":
                i2, i1 = inputs.pop(), inputs.pop()
                inputs.append(i1 - i2)
            elif i == "*":
                i2, i1 = inputs.pop(), inputs.pop()
                inputs.append(i1 * i2)
            elif i == "/":
                i2, i1 = inputs.pop(), inputs.pop()
                inputs.append(int(i1 / i2))
            else:
                inputs.append(int(i))
        
        return inputs.pop()
        
