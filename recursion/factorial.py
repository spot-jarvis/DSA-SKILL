def factorial(n:int) -> int:
    if n <= 1:
        return 1
    return n * factorial(n-1)

n = 4
res = factorial(n)
print(res)