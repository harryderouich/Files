#Harry Derouich
#13/02/15
#Files Class Exercises - Revision 1

with open("rev_1.txt",mode="w",encoding="utf-8") as my_file:
    for count in range(5):
        name = input("Enter line of text: ")
        my_file.write(name)
        my_file.write("\n")

