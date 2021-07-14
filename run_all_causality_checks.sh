#!/bin/bash

#for file in ../OSU_hydro/test_all/viscous_14_moments_evo.dat \
#			../MUSIC/v8/PbPb_*Kompost/results/evolution_full.dat
#do
#	sbatch --export=ALL,file_to_check=`realpath $file` run_causality_check_3_plus_1D.sbatch
#done

#for file in ../OSU_hydro/RESULTS_pPb_OPTIMAL/viscous_14_moments_evo.dat \
#			../MUSIC/v8/pPb_noKompost/results/evolution_full.dat \
#			../MUSIC/v8/OO_noKompost/results/evolution_full.dat
for file in ../OSU_hydro/RESULTS_pPb_OPTIMAL_nc6/viscous_14_moments_evo.dat \
do
	sbatch --export=ALL,file_to_check=`realpath $file` run_causality_check_3_plus_1D.sbatch
done
