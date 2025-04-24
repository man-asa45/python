def abc(a):
    if a==4:
       return
    a+=1
    abc(a)
    print( "CSE", end=" ")
    abc(a)
    print("mech", end=" ")
def main():
    num="12"
    for i in num:
         print()
         abc(int(a))
main()