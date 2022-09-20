def yes_no(question):

    error = "please awnser yes / no"

    valid = False
    while not valid:


        response = input(question).lower()

        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print(error)




for item in range(0, 6):
     want_snacks = yes_no("Do you want snacks? ")
     print("Awnser Ok, you said:", want_snacks)
     print()
