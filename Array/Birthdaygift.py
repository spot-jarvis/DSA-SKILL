def counter(n ,k):
    num = 0
    if k==1:
        return n
    else :
        for i in range(1,n+1):
            for j in range(1,n+1):
                if j % i == 0:
                    num += 1
    return num

def count(n,k):
    if k ==1:
        return n 
    if k == 2:
        return counter(n,k)
    mid = k //2
    x = count(n,k-mid)
    y = counter(n,mid)
    return x + y -1

n = int(input())
k = int(input())
print(count(n,k))
                    