# Guest lists program

guests = ['Ahamad', 'Nasima', 'Arezo', 'Karim']


print("Welcome to guest managment list app: ")

print("please choose from menu below")


while True:

    print("1:View Guests  2:Add Guest   3: Remove guest")

    choice = int(input("Enter your Choice "))

    while choice not in range(1, 4):

        print("Invalid choice selected, Please choose a number between 1-3  ")

        choice = int(input("Enter your Choice "))

    if choice == 1:

        for guest in guests:

            print(guest)

    elif choice == 2:

        name = input("Enter the guest name ")

        guests.append(name)

        print("updated guest lists")

    elif choice == 3:

        for index, name in enumerate(guests):

            print(index, name)

        remove_name = int(
            input("Enter the index assoicated to guest name to be removed: "))

        guests.pop(remove_name)


# print(guests)
