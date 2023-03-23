# -*- coding: utf-8 -*-
import glob
import os
import sys


 participant = pwsys.argv[1]

        
'''
    Checks for func, beh, anat, and fmap directories
    Creates them, if they do not exist.
            Parameters:
                    a) participant in f1XXXX format
                    b) directory up to and inclduding ses-1 
            Returns:
                    none
'''
def makedir(participant, directory):
    #check if directories exist, if not, create them
    if(not os.path.exists(directory + "/func/")):
        os.mkdir(directory + "/func/")
    if(not os.path.exists(directory + "/anat/")):
        os.mkdir(directory + "/anat/")
    if(not os.path.exists(directory + "/fmap/")):
        os.mkdir(directory + "/fmap/")
    if(not os.path.exists(directory + "/dti/")):
        os.mkdir(directory + "/dti/")

'''
    Renames files all per the file renaming document from Nina
            Parameters:
                    a) participant in f1XXXX format
                    b) directory up to and inclduding ses-1
            Returns:
                    none
'''
def rename_partic(participant, directory): 
    #search using glob on the pattern that Nina in the doc 
    print(participant + " " + directory)
    print("in rename partic")

    #FMAPS
    files = glob.glob(directory + "/" + participant + "--SpinEchoFieldMap_AP*")
    ap_dict = {}
    for file in files:
        index1 = file.index("AP") + 5
        index2 = file.index("--e1")
        scan_number = int(file[index1:index2])
        dict[scan_number] = file
    ap_sorted = dict(sorted(ap_dict.items()))
    counter = 1
    for scan, file in dict(sorted(ap_sorted.items()))
        print(file)
        parts = file.split(".", 1)
        new_name = "sub-" + participant + "_ses-1_run-" + counter + "_ap." + parts[1]
        print(directory + "/" + new_name)
        os.rename(file, directory + "/" + new_name) 


    files = glob.glob(directory + "/" + participant + "--SpinEchoFieldMap_PA*")
    pa_dict = []
    for file in files:
        index1 = file.index("PA") + 5
        index2 = file.index("--e1")
        scan_number = int(file[index1:index2])
        dict[scan_number] = file
    pa_sorted = dict(sorted(pa_dict.items()))
    counter = 1
    for scan, file in dict(sorted(pa_sorted.items()))
        print(file)
        parts = file.split(".", 1)
        new_name = "sub-" + participant + "_ses-1_run-" + counter + "_pa." + parts[1]
        print(directory + "/" + new_name)
        os.rename(file, directory + "/" + new_name) 

    #MID
    files = glob.glob(directory + "/" + participant + "--MID1--*") + glob.glob(directory + "/" + participant + "--MID1*")
    for file in files:
        print(file)
        parts = file.split(".", 1)
        new_name = "sub-" + participant + "_ses-1_task-mid_run-01_bold." + parts[1]
        print(directory + "/" + new_name)
        os.rename(file, directory + "/" + new_name) 
    files = glob.glob(directory + "/" + participant + "--MID2--*") + glob.glob(directory + "/" + participant + "--MID2*")
    for file in files:
        print(file)
        parts = file.split(".", 1)
        new_name = "sub-" + participant + "_ses-1_task-mid_run-02_bold." + parts[1]
        print(directory + "/" + new_name)
        os.rename(file, directory + "/" + new_name)  

    #REST1
    files = glob.glob(directory + "/" + participant + "--Resting_state_run_1*") 
    for file in files:
        print(file)
        parts = file.split(".", 1)
        new_name = "sub-" + participant + "_ses-1_task-rest_run-01_bold." + parts[1]
        print(directory + "/" + new_name)
        os.rename(file, directory + "/" + new_name) 
    #REST2
    files = glob.glob(directory + "/" + participant + "--Resting_state_run_2*") 
    for file in files:
        print(file)
        parts = file.split(".", 1)
        new_name = "sub-" + participant + "_ses-1_task-rest_run-02_bold." + parts[1]
        print(directory + "/" + new_name)
        os.rename(file, directory + "/" + new_name)  
    #REST3
    files = glob.glob(directory + "/" + participant + "--Resting_state_run_3*") 
    for file/ in files:
        print(file)
        parts = file.split(".", 1)
        new_name = "sub-" + participant + "_ses-1_task-rest_run-03_bold." + parts[1]
        print(directory + "/" + new_name)
        os.rename(file, directory + "/" + new_name) 
    #DTI
    files = glob.glob(directory + "/" + participant + "--mb4_1k_2k_64dir_1pt5mm--s*")
    for file in files:
        print(file)
        parts = file.split(".", 1)
        new_name = "sub-" + participant + "_ses-1_dwi." + parts[1]
        print(directory + "/" + new_name)
        os.rename(file, directory + "/" + new_name) 
    #T1W
    files = glob.glob(directory + "/" + participant + "--MPRAGE*") + glob.glob(directory + "/" + participant + "--T1w*")
    for file in files:
        print(file)
        parts = file.split(".", 1)
        new_name = "sub-" + participant + "_ses-1_run-1_T1w." + parts[1]
        print(directory + "/" + new_name)
        os.rename(file, directory + "/" + new_name) 

'''
    Moves files to their respective sub folders
            Parameters:
                    a) participant in f1XXXX format
                    b) directory up to and inclduding ses-1
            Returns:
                    none
'''   
def move_to_folders(participant, directory):
    #move functional files
    print("in move to folders")
    func_pattern = "sub-"+ participant + "_ses-1_task*"
    func_files = glob.glob(directory + "/" + func_pattern)
    for file in func_files:
        print(file)
        parts = file.split("/")
        os.rename(file, directory + "/func/" + parts[-1])
    #move anatomical files
    anat_pattern = "sub-"+ participant + "_ses-1_run-1_T1w*"
    anat_files = glob.glob(directory + "/" + anat_pattern)
    for file in anat_files:
        print(file)
        parts = file.split("/")
        os.rename(file, directory + "/anat/" + parts[-1])
    #move fmap files
    fmap_files = glob.glob(directory + "/sub*")
    for file in fmap_files:
        print(file)
        parts = file.split("/")
        os.rename(file, directory + "/fmap/" + parts[-1])



def main():
    key = participant
    value = "/projects/b1108/studies/transitions/data/raw/neuroimaging/bids/rename/sub-" + participant + "/ses-1" 
    makedir(key, value)
    rename_partic(key, value)
    move_to_folders(key, value)



if __name__ == "__main__":
    main()



