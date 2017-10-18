import os

rootDir = "."

for dirName, subDirList, fileList in os.walk(rootDir):
    print ("Dir: %s" %dirName)
    for fileName in fileList:
        print("\t%s" %fileName)
