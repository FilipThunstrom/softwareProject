import os 
import sys 
from RenameImageFile import RenameFileWithExifData

inputFolderPath = sys.argv[1]
outputFolderPath = sys.argv[2]

for filename in os.listdir(inputFolderPath): 
    filePath = inputFolderPath + "\\" + filename
    print(filePath)
    RenameFileWithExifData(filePath, outputFolderPath)
