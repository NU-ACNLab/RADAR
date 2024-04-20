import os
import glob
import json
import sys

#participant = sys.argv[1]

subjectsPath = "/Users/katharinaseitz/Documents/dicom_conversions/radar_bids_conversion/bids/sub-2895" #+ participant
subjects = glob.glob(subjectsPath)

for subject in subjects:
    print(subject)
    ID = subject.split("/")[-1]
    print(ID)
	#Edit 'ses-1' to be the same as your session
    fmapsPath = os.path.join(subject, 'ses-1', 'fmap', '*.json')
    fmaps = glob.glob(fmapsPath)
    funcsPath = os.path.join(subject, 'ses-1', 'func', '*.nii.gz')
    funcs = glob.glob(funcsPath)

	#substring to be removed from absolute path of functional files
    pathToRemove = subject + '/'
    funcs = list(map(lambda x: x.replace(pathToRemove, ''), funcs))
    print(funcs)
    for fmap in fmaps:
        with open(fmap, 'r') as data_file:
            fmap_json = json.load(data_file)
        if("run-1" in fmap):
            #resting state 1 and 2
            rest1 = funcs.index('ses-1/func/' + ID + "_ses-1_task-rest_run-01_bold.nii.gz")
            rest2 = funcs.index('ses-1/func/' + ID + "_ses-1_task-rest_run-02_bold.nii.gz")
            fmap_json['IntendedFor'] = [funcs[rest1], funcs[rest2]]
        elif("run-2" in fmap):
            #MID 1 and 2
            mid1 = funcs.index('ses-1/func/' + ID + "_ses-1_task-mid_run-01_bold.nii.gz")
            mid2 = funcs.index('ses-1/func/' + ID + "_ses-1_task-mid_run-02_bold.nii.gz")
            fmap_json['IntendedFor'] = [funcs[mid1], funcs[mid2]]
        elif("run-3" in fmap):
            #REST 3 and 4
            rest3 = funcs.index('ses-1/func/' + ID + "_ses-1_task-rest_run-03_bold.nii.gz")
            if('ses-1/func/' + ID + "_ses-1_task-rest_run-04_bold.nii.gz" in funcs):
                rest4 = funcs.index('ses-1/func/' + ID + "_ses-1_task-rest_run-04_bold.nii.gz")
                fmap_json['IntendedFor'] = [funcs[rest3], funcs[rest4]]
            else:
                fmap_json['IntendedFor'] = [funcs[rest3]]
        else:
            print("Inteded for failed for " + ID + "and fmap" + fmap)
        with open(fmap, 'w') as data_file:
            fmap_json = json.dump(fmap_json, data_file, indent=4)
			