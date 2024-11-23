# guest manager

guests = {}


guests["Jawid"] = ("Jawid", 20, "jaiwd@yahoo.com")

guests["Ahmad"] = ("Ahmad", 16, "ahmad@gmail.com")

guests["karim"] = ("Karim", 25, "karim@gmail.com")


def get_guest_info(name):

    if name in guests:

        info = guests[name]

        print(f"{info[0]} is in the guest list")

        print("Here is a full detail of the guest :")

        print("-------------------------------------")

        print(f" Guest Name : {info[0]}\n Guest Age: {info[1]}\n Guest email: {info[2]}")

    else:

        print("name is not in the guest list")


def get_all_guest_info():

    print("Guest Names:")

    for guest in guests:

        print(f" ", guest)

def remove_guest():
    name = input("Enter guest name to be removed: ")
    guests[name] = (name)
    if name == guests[name]:
        guests.pop(name)
        print(f"{name} deleted from list: ")
    else:
        print("Guest Name not found!!")

def add_guest():

    name = input("Enter guest name: ")

    age = int(input("Enter guest age: "))

    email = input("Enter guest email ")

    guests[name] = (name, age, email)

    print(f" {name} added to guest list: ")


# print(guests)
while True:

    choice = int(input(
        "Enter your Choice:\n 1:Search Guest\n 2:Add guest\n 3:view all guests\n 4:Remove a guest\n 5:Exit\n"))

    if choice == 1:

        guest_name = input("Enter guest name to search: ")

        get_guest_info(guest_name)

    elif choice == 2:

        add_guest()

    elif choice == 3:

        get_all_guest_info()
    elif choice == 4:
        remove_guest()

    elif choice == 5:

        print("exiting from the program! ")

        break

    else:

        print("Invalid input")
