#!/bin/bash

# Pb Pb - Vishnu
#for file in ../OSU_hydro/test_all/causality_check_w_characteristic_velocities.dat
#do
#	sbatch --export=ALL,causality_check_file=`readlink -e $file`,gridScale=16.7778,gridSize=$[235**2],eDecoupling=0.26511743083794326,dxy=0.1434 generate_char_vel_movie.sbatch
#done


# Pb Pb - MUSIC
#for file in ../MUSIC/v8/PbPb_*Kompost/results/causality_check_w_characteristic_velocities.dat
#do
#	sbatch --export=ALL,causality_check_file=`readlink -e $file`,gridScale=20.48,gridSize=$[512**2],eDecoupling=0.18,dxy=0.08 generate_char_vel_movie.sbatch
#done


# p Pb - Vishnu
for file in ../OSU_hydro/RESULTS_pPb_OPTIMAL/causality_check_w_characteristic_velocities.dat
do
	sbatch --export=ALL,causality_check_file=`readlink -e $file`,gridScale=7.182,gridSize=$[113**2],eDecoupling=0.26511743083794326,dxy=0.12825 generate_char_vel_movie.sbatch
done


# p Pb - MUSIC
for file in ../MUSIC/v8/pPb_noKompost/results/causality_check_w_characteristic_velocities.dat
do
	sbatch --export=ALL,causality_check_file=`readlink -e $file`,gridScale=10.0,gridSize=$[512**2],eDecoupling=0.18,dxy=0.0390625 generate_char_vel_movie.sbatch
done


# O O - MUSIC
for file in ../MUSIC/v8/OO_noKompost/results/causality_check_w_characteristic_velocities.dat
do
	sbatch --export=ALL,causality_check_file=`readlink -e $file`,gridScale=14.0,gridSize=$[512**2],eDecoupling=0.18,dxy=0.0546875 generate_char_vel_movie.sbatch
done

