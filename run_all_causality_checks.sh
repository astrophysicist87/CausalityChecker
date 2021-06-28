#!/bin/bash

sbatch --export=ALL,file_to_check=`realpath ../OSU_hydro/test_all/viscous_14_moments_evo.dat` run_causality_check.sbatch

for file in ../MUSIC/v8/PbPb_*Kompost/results/evolution_full.dat
do
	sbatch --export=ALL,file_to_check=`realpath $file` run_causality_check_3_plus_1D.sbatch
done
