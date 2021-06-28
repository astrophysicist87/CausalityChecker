#!/bin/bash

for file in ../OSU_hydro/test_all/viscous_14_moments_evo.dat ../MUSIC/v8/PbPb_*Kompost/results/evolution_full.dat
do
	sbatch --export=ALL,file_to_check=`realpath $file` run_causality_check_3_plus_1D.sbatch
done
