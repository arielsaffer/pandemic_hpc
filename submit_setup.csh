#!/bin/tcsh
#BSUB -n 1
#BSUB -W 10 # Short task, maximum 10 minutes
#BSUB -J config_setup
#BSUB -o errors_outputs/stdout.%J
#BSUB -e errors_outputs/stderr.%J
module load conda
conda activate /usr/local/usrapps/rkmeente/env_pandemic
python hpc/create_env_file.py
python global_config.py
python hpc/command_writer.py
conda deactivate
