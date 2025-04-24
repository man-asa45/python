def percentage(person):
    tot=sum(person["marks"])
    return tot/4 

a = [
    {"name": "RAJU", "age": 23, "marks": [45, 50, 40, 60]}, 
    {"name": "ROSE", "age": 12, "marks": [75, 85, 80, 90]}, 
    {"name": "RAVI", "age": 53, "marks": [65, 70, 60, 80]}, 
    {"name": "JACK", "age": 22, "marks": [55, 75, 65, 70]} 
    ]
b=sorted(a,key=percentage,reverse=True)

print(b)
l=["First","Second","Third","Fourth"]
pos=0
for i in b:
    print("{} has score {}% -----> stands {}".format(i["name"],percentage(i),l[pos]))
    pos=pos+1