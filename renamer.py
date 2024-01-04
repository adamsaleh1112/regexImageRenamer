import os # importing os which allows for path navigation and editing
import re # importing regex expressions
from serviceaccountpython import tospread # importing the spreadsheet function to write both the og and updated file names


renamedDict = [] # initializing a dictionary that will later be used to check for duplicate filenames
name = "AdamSaleh" # setting up a string that is my name so duplicate files can have an additional letter of my name added to them


# FILE RENAMER
def renamer(path): # path is specified by the user

    files = os.listdir(path) # turning the files in the path into a list
    format = re.compile(r'(IMG_|MMA|SM__|WJ2_)(\d+).JPG$', re.IGNORECASE) # setting up a regex compiler that checks for files beginning in img/dsc and ending with .jpg

    for file in files: # iterating through the files in the directory
        check = format.match(file) # checking if the file matches the format above

        if check: # if it does follow the format
            prefix, image_number = check.groups() # defining varibles for the formatting groups: prefix = (IMG|DSC), image_number = (\d+)
            renamedFile = f'PWP2024_000{image_number}A_ADAM.JPG' # defining the format of the renamed files
            of = os.path.join(path, file) # defining path of the original image that will be renamed

            count = 0 # initializing a variable that will determine how many letters of my name are used before _ADAM

            while renamedFile in renamedDict: # while the renamed file already exists in the dictionary

                count += 1 # add a letter of my name
                renamedFile = f'PWP2024_000{image_number}{name[:count]}_ADAM.JPG' # set new renamed file

            renamedDict.append(renamedFile) # append the new name to the dictionary to allow the loop to run later and check for duplicates once again

            nf = os.path.join(path, renamedFile) # setting new file path variable to the path + the new file name
            os.rename(of, nf) # replacing old file with new file using the new file path

    tospread(1, files) # writes og names to column 1 (A)
    tospread(2, renamedDict) # writes new names to column 2 (B)