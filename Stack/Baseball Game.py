class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []
        for i in range(len(operations)):
            if operations[i] == 'C':
                record.pop()
            elif operations[i] == 'D':
                double = record[-1] * 2
                record.append(double)
            elif operations[i] == '+':
                record.append(record[-1] + record[-2])
            else:
                record.append(int(operations[i]))
        return sum(record)

class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []
        for op in operations:
            if op == '+':
                record.append(record[-1]+record[-2])
            elif op == 'C':
                record.pop()
            elif op == 'D':
                record.append(2 * record[-1])
            else:
                record.append(int(op))
        return sum(record)