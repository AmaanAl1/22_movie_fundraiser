name = ""
count = 0
max_tickets = 5

while name != "xxx" and count < max_tickets:
    print("You have {} seats "
          "left".format(max_tickets - count))


    name = input("Name: ")
    count += 1
    print()

if count == max_tickets:
    print("you have sold all the available tickets")
else:
    print("you have sold {} tickets. \n"
          "there are {} places still available"
          .format(count, max_tickets - count))
