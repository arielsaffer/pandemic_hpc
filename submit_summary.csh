#!/bin/tcsh
#BSUB -n 2
#BSUB -x
#BSUB -R span[hosts=1]
#BSUB -R select[oc]
#BSUB -W 2:30 # Time depends on no. of runs aggregated
#BSUB -J summary_PoPSGlobal
#BSUB -o errors_outputs/stdout.%J
#BSUB -e errors_outputs/stderr.%J
module load conda
conda activate /usr/local/usrapps/rkmeente/env_pandemic
python  hpc/get_stats.py
conda deactivate
