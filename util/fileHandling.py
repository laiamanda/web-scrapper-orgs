import os

# Retrieve the location path of the main directory - Not Being Used
def getMainDirectory():
    # Retrieve the main Directory where the script is being ran at
    mainDirectory = os.path.abspath(os.getcwd())
    return mainDirectory

# Search for the Org File
def findOrgsFile():
    # Goes through every file and directories to see if the file exists
    if(os.path.exists("orgs.txt")): 
        return
    else :
        f = open("orgs.txt", "x")
        f.close()
        return
    
# Append items into Orgs File
def insertIntoFile():
    # Opens the Orgs File to Append
    f = open("orgs.txt", "a")
    # Dummy Values
    test = ['a', 'b', 'c']
    # Loop through Values
    for value in test:
        f.write(value + "\n")
    f.close()
    return