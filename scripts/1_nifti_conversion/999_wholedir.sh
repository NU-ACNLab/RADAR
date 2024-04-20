for DIR in /Users/katharinaseitz/Documents/dicom_conversions/radar_bids_conversion/dicoms/*; do
    BASE_DIR=$(basename $DIR)
    #[ -d "$dirs" ] && [ -n "$(ls -A $dirs)" ]
    if [ ! -d "/Users/katharinaseitz/Documents/dicom_conversions/radar_bids_conversion/bids/sub-$BASE_DIR/ses-1/anat" ]; then
        echo $BASE_DIR
        source /Users/katharinaseitz/Documents/dicom_conversions/radar_bids_conversion/99_dicom_to_bids_caller.sh $BASE_DIR
    fi 
done