
def printMenu():
    print("")
    print("1. Save a new entry")
    print("2. Search by ID")
    print("3. Print ages average")
    print("4. Print all names")
    print("5. Print all IDs")
    print("6. Print all entries")
    print("7. Print entry by index")
    print("8. Exit")


def printEntryDetails(id, entries):
    print("ID: " + str(id))
    print("Name: " + str(entries[id]["name"]))
    print("Age: " + str(entries[id]["age"]))


def saveNewEntry(entries, index_list):
    id_user = input("ID: ")
    if not id_user.isdigit():
        print("Error: ID must be a number. " + id_user + " is not a number ")
        return 0

    if id_user in entries:
        print("Error: ID already exists: " + str(entries[id_user]))
        return 0
    name_input = input("Name: ")
    age_input = input("Age: ")

    if not age_input.isdigit():
        print("Error: the age must be a number")
        return 0

    age_user = int(age_input)
    if age_user <= 15:
        print("Error: the age must be over 15")
        return 0

    entries[id_user] = {"name": name_input,"age": age_user}
    index_list.append(id_user)
    print("ID [" + id_user + "] saved successfully")
    return  age_user

def searchById(entries):
    wanted_id = input("Please enter the ID you want to look for: ")
    if wanted_id in entries:
       if wanted_id in entries:
        printEntryDetails(wanted_id, entries) # Function call
    elif not wanted_id.isdigit(): 
        print("Error: ID must be a number." + str(wanted_id) + " is not a number")
    else:
        print("Error: ID " + str(wanted_id) + " is not saved. ")

def printAgesAverage(total_ages,entries):
    if len(entries) == 0:
        print(0)
    else:
        average = total_ages / len(entries)
        print(average)

def printAllNames(entries):
    for index, entry in enumerate(entries.values()):
        print(str(index) + ". "  +  str(entry["name"]))

def printAllIds(entries):
    for index, key in enumerate(entries.keys()):
        print(str(index) + ". " + str(key))

def printAllEntries(entries):
    for index, (id_user, entry) in enumerate(entries.items()):
        print( str(index) +". " + str(id_user))
        print(" Name: " + str(entry["name"]))
        print( " Age: " + str(entry["age"])) 

def printEntryByIndex(entries, index_list):
    index_to_return = input("please enter the index of entry you want to print: ")
    
    if not index_to_return.isdigit():
        print("Error: index must be a number. " + index_to_return + " is not a number ")
        return 
    
    index_to_return = int(index_to_return)
    last_index = len(entries) - 1
    if index_to_return < 0 or index_to_return > last_index:
        print ("Error: index out of range. the maximum index allowed is " + str(last_index))
        return
    
    id = index_list[index_to_return]
    printEntryDetails(id, entries) # Function call
    

def exitProgramEntries():
    while True:
        exit_input = input("are you sure? y/n ") 
        if exit_input == "n":
            return False
        elif exit_input == "y":
            print("Goodbye!") 
            return True



def main():

    entries = {}
    index_list = []
    total_ages = 0
    while True:
        printMenu()
        choice = input("Please enter your choice: ")
        if choice == "1":
            total_ages += saveNewEntry(entries, index_list)
        elif choice == "2":
            searchById(entries)
        elif choice == "3":
            printAgesAverage(total_ages, entries)
        elif choice == "4":
            printAllNames(entries)
        elif choice == "5":
            printAllIds(entries)
        elif choice == "6":
            printAllEntries(entries)
        elif choice == "7":
            printEntryByIndex(entries, index_list)
        elif choice == "8":
            if exitProgramEntries() == True:
                break
        elif  int(choice) > 8:
            print("Error: option " + choice + " does not exist. please try again ") 
        input("Press Enter to continue ")
        
main()
