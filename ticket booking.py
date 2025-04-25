from datetime import datetime
class Bus:
    def __init__(self,bno,AC,cap):
        self.bno=bno
        self.AC=AC 
        self.cap=cap
        
    def get_bno(self):
        return self.bno 
    def get_AC(self):
        return self.AC 
    def get_cap(self):
        return self.cap
    def display(self):
        print("BusNo {} : AC {} : capacity is {}".format(self.bno,self.AC,self.cap))


class Bookings:
    def __init__(self):
        self.name=" "
        self.date=None
        self.bno=None
    def make_bookings(self,BUSES,BOOKINGS):
        self.name=input("enter passenger name")
        self.bno=int(input("Enter the Bus no.:"))
        d=input("enter the date in dd-mm-yyyy")
        self.date=datetime.strptime(d,"%d-%m-%Y").date()
        
        
        if(self.isavailable(BUSES,BOOKINGS,self.bno,self.date)):
             BOOKINGS.append(self)
             print("YOUR SEAT IS CONFORMED")
        else:
             print("full you can try another bus or date")
             
             
    def isavailable(self,BUSES,BOOKINGS,bno,date):
        capacity=0 
        booked=0 
        for i in BUSES:
            if(bno==i.bno):
                capacity=i.cap
        for j in BOOKINGS:
            if(date==j.date and bno==j.bno):
                booked=booked+1
        return booked<capacity

def main():
    BUSES=[Bus(100,True,2),Bus(200,False,50),Bus(300,False,48)]
    BOOKINGS=[]
    for i in BUSES:
        i.display()
    while True:
        opt=int(input("enter 1 to book , 2 to exit"))
        if(opt==1):
            book=Bookings()
            book.make_bookings(BUSES,BOOKINGS)
        else:
            break 
    



if __name__=="__main__":
    main() #ticket booking



