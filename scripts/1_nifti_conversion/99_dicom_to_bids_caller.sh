DIR=$1 #check if $ needed. 
echo $DIR

#Pipeline calls, one after another. 
source 1_dicom_nifti_convert.sh $DIR
python 2_rename_to_bids.py $DIR
source 3_deface.sh $DIR
python 4_add_intended_for.py $DIR





