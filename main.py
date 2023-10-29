
my_name_list = []


def add_name(): #This function adds comma separated names or single names to the list

    name = input("Please add your name : ")
    splittedword = name.split(",")
    if name == "":
        print("Name save it succesfully")
    else:
        add_name()
        for word in splittedword:
            my_name_list.append(word)


def serach_name_for_index():       #This function allows you serach to index by name
    index = int(input("Which name do you want ?")) - 1
    if index <= len(my_name_list):
        print("------------------------------")
        print(my_name_list[index])
    else:
        print("You have logged in more than your number of users..")
        print("------------------------------")


def serach_for_name():      #This function allows you to search by name
    serach_name = input("Enter the name you want to check:")
    print("------------------------------")
    if serach_name in my_name_list:
        print("The name is available in your list. The name you are looking for :", end="")
        print(serach_name)

    else:
        print("The name is not in your list.")
        print("------------------------------")


def length_list():  #This function counts the number of elements in the list
    len(my_name_list)
    print("------------------------------")
    print(len(my_name_list))


def show_list():        #This function show the all list elements
    print("------------------------------")
    print(my_name_list)


def print_commands():
    print("----------------------------")
    print("Name List Application")

    print("1.Add name")
    print("2.Check a name whose sequence number you know. ")
    print("3.Which name do you want to check ?")
    print("4.How many people are on the list ?")
    print("5.Show full list.")


def choice():   ##This function makes the user choose what they want to do

    choice = int(input("Make your choice ?"))

    if choice == 1:
        add_name()
    elif choice == 2:
        serach_name_for_index()
    elif choice == 3:
        serach_for_name()
    elif choice == 4:
        length_list()
    elif choice == 5:
        show_list()
    else:
        print("invalid choice")


while True:

    print_commands()
    print("Make your chocie (1/2/3/4/5)")
    choice()


