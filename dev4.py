#Harry Derouich
#13/02/15
#Files Class Exercises - Development 4

import pickle

class DataRecord:
    def __init__(self):
        self.Name = None
        self.dob = None


with open("dev_2.dat", mode = "rb") as my_file:
    current_records = pickle.load(my_file)


for x in current_records:
    print("Name:",x.Name)
    print("Date of birth:" ,x.dob[:2]+"/"+x.dob[2:4]+"/"+x.dob[4:])
    print("")
