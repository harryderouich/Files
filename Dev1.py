#Harry Derouich
#13/02/15
#Files Class Exercises - Development 1

import pickle

with open("dev_1.dat", mode = "wb") as personal_records:
    datarecord = []
    name = input("Please enter your name: ")
    date_birth = input("Please enter your date of birth DDMMYY: ")
    datarecord.append(name)
    datarecord.append(date_birth)

    pickle.dump(datarecord,personal_records)
