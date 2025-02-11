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
def insertIntoFile(companyName):
    # my_list = ['Dejan Živković','Gregg Berhalter','James Stevens','Mike Windischmann',
    #             'Gunnar Heiðar Þorvaldsson']
    
    # # Opens the Orgs File to Append
    # with open("newOrgs.txt", "a", encoding="utf-8") as file:
    #     file.writelines( "%s\n" % item for item in my_list )
    
   # Opens the Orgs File to Append
    with open("orgs.txt", "a", encoding="utf-8") as file:
        # Able to write each company name. Can handle non-ascii code
        file.write( "%s\n" % companyName )
    return