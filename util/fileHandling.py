import os
import glob

# Retrieve the location path of the main directory - Not Being Used
def getMainDirectory():
    # Retrieve the main Directory where the script is being ran at
    mainDirectory = os.path.abspath(os.getcwd())

# Search for the Org File
def findOrgsFile():
    # Goes through every file and directories to see if the file exists
    if(os.path.exists("orgs.txt")): 
        return
    else :
        f = open("orgs.txt", "x")
        f.close()

def insertIntoFile():
    test = ['a', 'b', 'c']
    for value in test:
        print(value) 