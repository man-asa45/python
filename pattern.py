n=int(input("Enter any number "))
num=1
for i in range(1,n+1):
    if(i%2!=0):
        for j in range(1,i+1):
            print(num, end=" ")
            num=num+1
            if(j<i):
                print("*", end=" ")
        print()
    else:
        temp=num+(i-1)
        for j in range(1,i+1):
            print(temp,end=" ")
            if(j<i):
                print("*", end=" ")
            temp=temp-1
            num=num+1
        print()