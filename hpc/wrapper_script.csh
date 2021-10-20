#!/bin/tcsh
# Script: wrapper_script.csh (individual sample)

# Set the path for the temporary file directory
# $LSB_JOBID will reference the job ID of the submission
setenv TEMPDIR /scratch/$LSB_JOBID

# Create the directory 
mkdir -p $TEMPDIR/temp_outputs

# Run code
# Note that $argv:q is necessary to pass arguments from the tasks file to the code you want to run
module load conda
conda activate /usr/local/usrapps/rkmeente/env_pandemic
python model_run_args.py $argv:q $TEMPDIR

# then run summary stats on outputs in temp, but write  to the non-temp directory
python ./hpc/get_stats.py $TEMPDIR/temp_outputs
conda deactivate

# Remove the temporary files and directory
rm -fr $TEMPDIR