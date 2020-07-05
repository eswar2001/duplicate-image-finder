from PIL import Image
import imagehash
import os


file_ext = [".JPG",
            ".JFIF",
            ".JPEG",
            ".Exif",
            ".TIFF",
            ".GIF",
            ".BMP",
            ".PNG",
            ".PPM",
            ".PGM",
            ".PBM",
            ".PNM",
            ".WebP",
            ".CGM",
            ".SVG"]
file_list = []
hash_set = set([])
dummy = []


def generate_hash():
    a = len(file_list)
    b = 0
    for i in file_list:
        d = (b/a)*100
        print(d)
        hash = imagehash.average_hash(Image.open(i))
        size = len(hash_set)
        hash_set.add(hash)
        if size == len(hash_set):
            dummy.append(i)
        b = b+1


def print_list():
    for i in dummy:
        print(i)


def check_img(fullPath):
    ext = os.path.splitext(fullPath)
    for i in file_ext:
        if(i.lower() == ext[1].lower()):
            file_list.append(fullPath)
            return bool(1)
    return bool(0)


def getListOfFiles(dirName):
    # create a list of file and sub directories
    # names in the given directory
    listOfFile = os.listdir(dirName)
    allFiles = list()
    # Iterate over all the entries
    for entry in listOfFile:
        # Create full path
        fullPath = os.path.join(dirName, entry)
        # If entry is a directory then get the list of files in this directory
        if os.path.isdir(fullPath):
            allFiles = allFiles + getListOfFiles(fullPath)
        else:
            if (check_img(fullPath)):
                allFiles.append(fullPath)

    return allFiles


dirName = os.getcwd()
listOfFiles = getListOfFiles(dirName)
listOfFiles = list()
for (dirpath, dirname, filenames) in os.walk(dirName):
    listOfFiles += [os.path.join(dirpath, file) for file in filenames]
generate_hash()
print_list()
