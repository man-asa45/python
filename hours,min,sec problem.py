import time
h,m,s=4,3,0
while(1):
    time.sleep(1)
    s=s+1
    if(s==60):
        s=0 
        m=m+1 
    elif(m==60):
        s=0 
        h=h+1 
        m=0 
    elif(h==12):
        s=0 
        m=0 
        h=0 
    print("{} : {} : {}".format(h,m,s))