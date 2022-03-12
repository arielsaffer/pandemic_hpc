#!/bin/csh
#BSUB -W 2:30		   # e.g. Maximum 2 hrs 30 min (~5 min per run, per core (-n))
#BSUB -J popsGlobal     # Job name as listed in queue
#BSUB -n 51	   # number of MPI processes (1 core reserved for pynodelauncher)
#BSUB -oo errors_outputs/popsGlobal_out   # Write stdout, overwrite old ones
#BSUB -eo errors_outputs/popsGlobal_err   # Write stdout, overwrite old ones
module load PrgEnv-intel
module load conda
conda activate /usr/local/usrapps/rkmeente/env_pandemic
mpirun ../launch/launch commands.txt
conda deactivate