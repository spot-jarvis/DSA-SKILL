class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
        
        n,m = len(num1),len(num2)
        result = [0] * (n+m)

        for i in range(n-1,-1,-1):
            dig1 = int(num1[i])
            for j in range(m-1,-1,-1):
                dig2 = int(num2[j])

                pos = i+j+1
                product = dig1 * dig2 + result[pos]
                result[pos] = product % 10
                result[pos-1] += product // 10

        k =0
        while k < len(result) and result[k] == 0:
            k+=1

        return "".join(str(d) for d in result[k:])