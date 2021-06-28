#!/bin/bash
#----------

# Free parameters:
#   file:          file to process							(argument 1)
#   inGridScale:   max value along x and y axes [fm]		(argument 2)
#   inGridSize:    total number of grid points				(argument 3)
#   inEDecoupling: eFO [GeV/fm^]							(argument 4)
#   inDXY:         grid spacing [fm]						(argument 5)


#for file in ../MUSIC/results/evolution_full.dat
for file in "$1"
do
	path=`readlink -e $file`
	#sbatch --export=ALL,file_to_check=`echo $path`,inGridScale=20.48,inGridSize=$[512**2],inEDecoupling=0.3,inDXY=0.08 run_all.sbatch
	sbatch --export=ALL,file_to_check=`echo $path`,inGridScale=$2,inGridSize=$3,inEDecoupling=$4,inDXY=$5 run_all.sbatch
done

