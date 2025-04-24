def prime(n):
    if n==1:
        return []
    for i in range(2,n+1):
       if n%i==0:
          return[i]+prime(n//i)
n=int(input())
print(prime(n))
