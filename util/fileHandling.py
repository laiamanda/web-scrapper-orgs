import os
from util import db

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
def insertIntoFile(companyName):
   # Opens the Orgs File to Append
    with open("orgs.txt", "a", encoding="utf-8") as file:
        # Able to write each company name. Can handle non-ascii code
        file.write( "%s\n" % companyName )
    return

# Read the Orgs File
def readFile():
    with open("orgs.txt","r", encoding="utf-8") as file:
        for name in file:
            # Insert each name from the text file to the database
            db.insertDatabase(name)
    