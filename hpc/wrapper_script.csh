#!/bin/tcsh
# Script: wrapper_script.csh (individual sample)

# Create the directory 
mkdir -p /scratch/temp_outputs/samp$1_$2_$3

# Set the path for the temporary file directory
setenv TMPDIR /scratch/temp_outputs/samp$1_$2_$3

# Run code
# Note that $argv:q is necessary to pass arguments from the tasks file to the code you want to run
module load conda
conda activate /usr/local/usrapps/rkmeente/env_pandemic
python model_run_args.py $argv:q

# then run summary stats on outputs in temp, but write to the non-temp directory
python ./hpc/get_stats.py $argv:q
conda deactivate

# Remove the temporary files and directory
rm -fr $TMPDIR