#!/bin/bash

# p Pb - Vishnu
for file in ../OSU_hydro/RESULTS_pPb_OPTIMAL_nc6/causality_check.dat
do
	sbatch --export=ALL,causality_check_file=`readlink -e $file`,gridScale=6.7725,gridSize=$[211**2],eDecoupling=0.26511743083794326,dxy=0.0645 generate_movie.sbatch
done
