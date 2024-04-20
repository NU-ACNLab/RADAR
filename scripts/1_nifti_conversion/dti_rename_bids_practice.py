import glob #good for finding files
import os
import sys
import json



participant = "3423"
directory = "bids/sub-" + participant + "/ses-1"
#DTI

files = glob.glob(directory + "/*" + participant + "--mb4_1k_2k_64dir_1pt5mm--s*") #TODO: change the "--mb4_..." to match the TRACE file format. 
for file in files:
    print(file)
    parts = file.split(".", 1) #string formatting, splits strings into pieces based on passed in character
    new_name = "sub-" + participant + "_ses-1_run-1_dwi." + parts[1] #defined new_name string by concatinating characters
    print(directory + "/" + new_name) #prints the path + the new name
    os.rename(file, directory + "/" + new_name) #uses the os command to rename the file...