students={4 :{"name":"manasa","cgpa":9,"dept":"cse","gender":"female"},
          5 :{"name":"aa","cgpa":8.8,"dept":"csd","gender":"male"},
          6 :{"name":"bb","cgpa":9.4,"dept":"csm","gender":"male"},
          7 :{"name":"ss","cgpa":6,"dept":"cso","gender":"female"}}
print("-"*38)
print("|{:10}|{:<12}|{:<7}|{:<7}|{:<7}|".format("id","name","cgpa","dept","gender"))

print("-"*38)
for id,info in students.items():
    print("|{:<10}|{:<12}|{:<7}|{:<7}|{:<7}|".format((id),info["name"],info["cgpa"],info["dept"],info["gender"]))