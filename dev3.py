#Harry Derouich
#13/02/15
#Files Class Exercises - Development 3


import pickle

with open("dev_1.dat", mode = "rb") as my_file:
    test = pickle.load(my_file)
    print("Name:",test[0])
    print("Date of Birth:",test[1][:2] + "/" + test[1][2:4] + "/" + test[1][4:])
