class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0]*len(temperatures)
        stack = [] # pair stack it store the value and index

        for i,temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                stackTem,stackInd = stack.pop()
                res[stackInd] = i - stackInd
            stack.append((temp,i))
        return res



""""
These is a brutal approach but it shows time limit exceed in larger inputs
n = len(temperatures)
        answer = []
        for i in range(n):
            for day_waited ,temp in enumerate(temperatures[i+1:],start =1):
                if temp > temperatures[i]:
                    answer.append(day_waited)
                    break
            else:
                    answer.append(0)
        return answer
"""