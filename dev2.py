#Harry Derouich
#13/02/15
#Files Class Exercises - Development 2

import pickle

class DataRecord:
    def __init__(self):
        self.Name = None
        self.dob = None


records = []


with open("dev_2.dat", mode = "wb") as personal_records:
    completed = False
    name = "x"
    while completed == False:
        name = input("Please enter your name (press enter to end): ")
        if name != "":
            record = DataRecord()
            date = input("Please enter your DoB DDMYY: ")
            record.Name = name
            record.dob = date
            records.append(record)
        else:
            completed = True
    pickle.dump(records,personal_records)
