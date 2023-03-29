#!/usr/bin/bash

#SBATCH -A p31833
#SBATCH -p normal
#SBATCH -t 48:00:00
#SBATCH --mem=64G
#SBATCH -J fmriprep_RADAR

module purge
module load singularity/latest
echo "modules loaded" 
cd /projects/b1108
pwd
echo "beginning preprocessing"

singularity run --cleanenv -B /projects/b1108:/projects/b1108 /projects/b1108/software/singularity_images/fmriprep-22.1.1.simg \
/projects/b1108/studies/RADAR/data/raw/neuroimaging/bids \
/projects/b1108/studies/RADAR/data/processed/neuroimaging/fmriprep/ \
participant --participant-label ${1} --fs-license-file \
/projects/b1108/software/freesurfer_license/license.txt -w /projects/b1108/studies/rise/data/processed/neuroimaging/fmriprep/work --skip_bids_validation
