from math import gcd
def coprime(i,j):
    return gcd(i,j)==1

a=int(input("Enter any num "))

for i in range(5,a):
    for j in range(4,i):
        for k in range(3,j):
            if(k*k + j*j==i*i) and coprime(i,j) and coprime(j,k) and coprime(i,k):
                print(k,j,i)