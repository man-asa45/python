A=1234
B=3454
C=7976
def big(n):
    return max(int(d) for d in str(n))
def sm(n):
    return min(int(d) for d in str(n))
a1=big(A)+big(B)+big(C)
a2=sm(A)+sm(B)+sm(C)
print(a1)
print(a2)
print(a1+a2)