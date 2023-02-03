import os
import shutil
import path_constant

srcfolder =  os.listdir(path_constant.TEST_PATH)

def main():
    #when camera is plugged in, run script
        #needs to scan for the mac address

    print("Source Folder:" + str(srcfolder))
    print()

    try:
        for i in srcfolder:
            currentFolder = path_constant.TEST_PATH + i + '\\'
            newFolder = path_constant.TEST_PATH + "newphotos" + '\\'
            print("Current Folder: " + currentFolder + "\n" + "New Folder: " + newFolder)

            
            print()
       
            shutil.copytree(currentFolder, newFolder, dirs_exist_ok=True)
            contentadded = os.listdir(newFolder)
            print("Images Added:" + str(contentadded))
            print()
    except:
        print("Failed to Move Images")


    #for timestamp of photo 1 iterate until photo upto timestamp + 24 hours
    #append to photo name list
    #.move photo to folder of that timestamp
    #remove photos that do no have faces
    #api call to google photos
    #create album and upload photos
    #create sharing url
    #send a text when completed to then set name
    #if face is know, send a text to person with sharing url
if __name__ == "__main__":
    main()
