#This is a comment, and won't be read by the interpreter

#this takes a user input and assigns it to the SUB folder
SUB=$1
echo $SUB #echo prints out the sub variable in the terminal.
#looks for the dicoms based on the participant
scan_folders=/Users/katharinaseitz/Documents/dicom_conversions/radar_bids_conversion/dicoms/$SUB/* 
echo $scan_folders
if [ ! -d "/Users/katharinaseitz/Documents/dicom_conversions/radar_bids_conversion/bids/sub-$SUB" ]; then
    mkdir /Users/katharinaseitz/Documents/dicom_conversions/radar_bids_conversion/bids/sub-$SUB
fi
if [ ! -d "/Users/katharinaseitz/Documents/dicom_conversions/radar_bids_conversion/bids/sub-$SUB/ses-1" ]; then
    mkdir /Users/katharinaseitz/Documents/dicom_conversions/radar_bids_conversion/bids/sub-$SUB/ses-1     
fi

# iterate through each of the sub folders inside the dicom/participant folder
# and convert to nifti and json pair
for SCAN in $scan_folders; do 
    echo $SCAN
    OUTPUT=/Users/katharinaseitz/Documents/dicom_conversions/radar_bids_conversion/bids/sub-$SUB/ses-1
    echo $OUTPUT
    dcm2niix -b y -z o -w 1 -f %n--%d--s%s--e%e -o $OUTPUT $SCAN
done

