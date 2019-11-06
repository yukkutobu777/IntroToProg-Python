# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# Kbosworth,11/04/19,Read in file
# Kbosworth,11/05/19,Add and remove items and then write to file. Tidy up code.
# ------------------------------------------------------------------------ #

# -- Data -- #
# declare variables and constants
objFile = "ToDoList.txt"  # An object that represents a file
strData = "ToDoList.txt"  # A row of text data from the file
dicRow = {}    # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A dictionary that acts as a 'table' of rows
# strMenu = ""   # A menu of user options (Kbosworth - I did not end up using this...)
strChoice = "" # A Capture the user option selection

# -- Processing -- #
# Step 1 - When the program starts, load the any data you have
# in a text file called ToDoList.txt into a python Dictionary.
objFile = open(strData, "r")
for row in objFile:
    lstRow = row.split(",")  # Returns a list!
    dicRow = {"task":lstRow[0],"priority":lstRow[1].strip()}
    lstTable.append(dicRow)
objFile.close()

# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
while (True):
    print("""
    Menu of Options:
    1) Show current data.
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File.
    5) Exit Program.
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print()  # adding a new line for looks
    # Step 3 - Show the current items in the table
    if (strChoice.strip() == '1'):
        for row in lstTable:
             print(row['task'] + ',' + row['priority'])
        continue
    # Step 4 - Add a new item to the list/Table
    elif (strChoice.strip() == '2'):
        task = input('Enter a task: ')
        priority = input('Enter a priority: ')
        dicRow = {"task":task,"priority":priority}
        lstTable.append(dicRow)
        continue
    # Step 5 - Remove a new item to the list/Table
    elif (strChoice.strip() == '3'):
        removeTask = input('Enter a task: ')
        removePriority = input('Enter a priority: ')
        lstTable.remove({'task':removeTask, 'priority':removePriority})
        continue
    # Step 6 - Save tasks to the ToDoToDoList.txt file
    elif (strChoice.strip() == '4'):
         objFile = open(strData, "w")
         for row in lstTable:
             objFile.write(row['task'] + ',' + row['priority'] + '\n')
         continue
    # Step 7 - Exit program
    elif (strChoice.strip() == '5'):
        objFile.close()
        break  # and Exit the program