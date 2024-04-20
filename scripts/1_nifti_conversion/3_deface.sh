SUB=$1 #check if $ needed. 
echo $SUB


pydeface --verbose /Users/katharinaseitz/Documents/dicom_conversions/radar_bids_conversion/bids/sub-$SUB/ses-1/anat/sub-${SUB}_ses-1_run-1_T1w.nii.gz 
mv /Users/katharinaseitz/Documents/dicom_conversions/radar_bids_conversion/bids/sub-$SUB/ses-1/anat/sub-${SUB}_ses-1_run-1_T1w_defaced.nii.gz \
/Users/katharinaseitz/Documents/dicom_conversions/radar_bids_conversion/bids/sub-$SUB/ses-1/anat/sub-${SUB}_ses-1_run-1_T1w.nii.gz
#rm /Users/katharinaseitz/Documents/dicom_conversions/radar_bids_conversion/bids/sub-$SUB/ses-1/${SUB}-*