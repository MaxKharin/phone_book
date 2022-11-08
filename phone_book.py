import time
import string
import secrets

print()
print("Telephone directory")

# создание файла
filename = "Tel_book.csv"
myfile = open(filename, "a+")
myfile.close


# метод главного меню
def main_menu():
    print("\nMain menu\n")
    print("1. All contacts")
    print("2. Add a new contact")
    print("3. Find an existing contact")
    print("4. Exit")
    choice = input(": ")
    if choice == "1":
        myfile = open(filename, "r+")
        filecontents = myfile.read()
        if len(filecontents) == 0:
            print("Contact not found")
        else:
            print(filecontents)
        myfile.close
        enter = input("Press Enter to continue")
        main_menu()
    elif choice == "2":
        newcontact()
        enter = input("Press Enter to continue")
        main_menu()
    elif choice == "3":
        searchcontact()
        enter = input("Press Enter to continue")
        main_menu()
    elif choice == "4":
        print("Goodbye!")
    else:
        print("Enter again\n")
        enter = input("Press Enter to continue")
        main_menu()


# метод поиска
def searchcontact():
    searchname = input("Enter the contact's NAME ")
    remname = searchname[1:]
    firstchar = searchname[0]
    searchname = firstchar.upper() + remname
    myfile = open(filename, "r+")
    filecontents = myfile.readlines()

    found = False
    for line in filecontents:
        if searchname in line:
            print("Found contact: ", end=" ")
            print(line)
            found = True
            break
    if found == False:
        print(f"The {searchname} contact was not found")

    # имя


def input_firstname():
    first = input("Enter your first name: ")
    remfname = first[1:]
    firstchar = first[0]
    return firstchar.upper() + remfname


# фамилия
def input_lastname():
    last = input("Enter your last name: ")
    remlname = last[1:]
    firstchar = last[0]
    return firstchar.upper() + remlname


# метод генерации ключа
def key_gen():
    alphabet = string.ascii_letters + string.digits
    key = ''.join(secrets.choice(alphabet) for i in range(4))
    return key


key = key_gen()


# сохранение новых данных контакта
def newcontact():
    firstname = input_firstname()
    lastname = input_lastname()
    phoneNum = input("Enter your phone number: ")
    emailID = input("Enter your E-mail: ")
    contactDetails = (f"{key};" + firstname + " " + lastname + ";" + phoneNum + ";" + emailID + "\n")
    myfile = open(filename, "a")
    myfile.write(contactDetails)
    print("New contact: \n " + contactDetails + " has been added to the book")


main_menu()
time.sleep(5)