def not_blank(question):
     valid  = False

     while not valid:
         response = input(question)

         if response != "":
             return response
         else:
             print("Sorry - this cant be blank"
                   "Please enter your name: ")

def int_check(question):
    error = "please enter a number more than 12 and less than 130"

    valid = False
    while not valid:
        try:
            response = int(input(question))

            if response <= 0:
                print(error)
            else:
                return response

        except ValueError:
            print(error)

name = ""
count = 0
max_tickets = 5

while name != "xxx" and count < max_tickets:

    if count < 4:
        print("you have {} seats "
              "left".format(max_tickets - count))
    else:
        print("***There is ONE seat left***")

    name = not_blank("Name: ")

    if name == "xxx":
        break

    age = int_check("Age: ")

    if age < 12:
        print("sorry you are too young for this movie")
        continue
    elif age > 130:
        print("that is very old it looks like a mistake has been made")
        continue

    count += 1


if count == max_tickets:
    print("you have sold all the available tickets")
else:
    print("you have sold {} tickets. \n"
          "there are {} places still available"
          .format(count, max_tickets - count))



