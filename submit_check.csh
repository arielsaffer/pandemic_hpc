#!/bin/tcsh
#BSUB -n 2
#BSUB -x
#BSUB -R span[hosts=1]
#BSUB -R select[oc]
#BSUB -W 2:30
#BSUB -J summary_PoPSGlobal
#BSUB -o stdout.%J
#BSUB -e stderr.%J
module load conda
conda activate /usr/local/usrapps/rkmeente/env_pandemic
python  hpc/run_checker.py
conda deactivate
