#!/bin/bash

for file in ../OSU_hydro/test_all/causality_check_w_characteristic_velocities.dat
do
	sbatch --export=ALL,causality_check_file=`readlink -e $file`,gridScale=16.7778,gridSize=$[235**2],eDecoupling=0.26511743083794326,dxy=0.1434 generate_char_vel_movie.sbatch
done



for file in ../MUSIC/v8/PbPb_*Kompost/results/causality_check_w_characteristic_velocities.dat
do
	sbatch --export=ALL,causality_check_file=`readlink -e $file`,gridScale=20.48,gridSize=$[512**2],eDecoupling=0.18,dxy=0.08 generate_char_vel_movie.sbatch
done
