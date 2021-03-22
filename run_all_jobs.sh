#!/bin/bash
#----------

# Free parameters:
#   file:          file to process
#   inGridScale:   max value along x and y axes [fm]
#   inGridSize:    total number of grid points
#   inEDecoupling: eFO [GeV/fm^]
#   inDXY:         grid spacing [fm]


for file in ../MUSIC/results/evolution_full.dat
do
        path=`readlink -e $file`
	sbatch --export=ALL,file_to_check=`echo $path`,inGridScale=20.48,inGridSize=$[512**2],inEDecoupling=0.3,inDXY=0.08 run_all.sbatch
done

