#!/usr/bin/env bash
#SBATCH -t 16:00:00                  # Job run time (hh:mm:ss)
#SBATCH -N 1                        # Number of nodes
#SBATCH -J serial_job            # Name of batch job
#SBATCH -A qgp
#SBATCH -p qgp
#SBATCH --output=generate_movie.out              # Name of batch job output file

echo 'Starting...'
bash generate_movie.sh $causality_check_file $gridScale $gridSize $eDecoupling $dxy
echo 'Finished!'
