#Harry Derouich
#Files R+R - Task 1

##index = 1
##with open("students.txt", mode="r", encoding="utf-8") as my_file:
##    for line in my_file:
##        print("{0}. {1}".format(index,line))
##        index = index + 1


with open("students.txt", mode="w", encoding="utf-8") as file:
        name = 'Name List:'
        while name != '-1':
            name = input("Please enter student name, -1 to stop: ")
            file.write(name)
            file.write("\n")
