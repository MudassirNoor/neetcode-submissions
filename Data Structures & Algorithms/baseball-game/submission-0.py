class Solution:
    def calPoints(self, operations: List[str]) -> int:
        if operations == None or len(operations) == 0:
            return 0

        records = []
        for op in operations:
            match op:
                case "+":
                # Add last 2
                    records.append(records[-1] + records[-2])
                case "D":
                # 2x last score
                    records.append(2 * records[-1])
                case "C":
                # remove last score
                    records.pop()
                case _:
                    records.append(int(op))
                    
        return sum(records)