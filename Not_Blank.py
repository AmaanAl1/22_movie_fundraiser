#---Function---
def not_blank(question,error):

# ---this section is a Loop that will force a Valid Input---
    valid  = False
    while not valid:
        response = input(question)
        if response == "":
            print(error)
        else:
            return response
#---this section is the Main Routine---
name = not_blank("Enter your name:  ", "Cannot be blank")
print("You entered {}".format(name))
