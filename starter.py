try:
    score = int(input("Please enter your score: "))
    print("Your score was {0}".format(score))
except ValueError:
    print("Please enter an integer value only")

