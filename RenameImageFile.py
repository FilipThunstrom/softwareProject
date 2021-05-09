import os
import shutil
import sys

from PIL import Image
from PIL.ExifTags import TAGS


def RenameFileWithExifData(filePath, outputFolder):
    # Pull the exif data from the file (date and time).
    image = Image.open(filePath)
    exifdata = image.getexif()

    exif = {
    TAGS[k]: v
    for k, v in exifdata.items()
    if k in TAGS
    }

    dateTime = exif['DateTime']
    dateTime = dateTime.replace(":", "-")

    # Copy the file to outputFolder.
    outputFilePath = outputFolder + '\\' + dateTime + ".jpg"
    print(outputFilePath)
    shutil.copy(filePath, outputFilePath)