#!/bin/bash

cd /projects/jnorhos/plumberg/MUSIC/v8
for direc in *
do
	echo 'Processing' $direc
	python3 /projects/jnorhos/plumberg/CausalityChecker/plot_hyperbol_viol_vs_tau_e.py 1 ${direc}/results/char_vel_frames/*
	cp ${direc}/results/hyperbol_viol_density_plot.png \
	   ${direc}/results/hyperbol_viol_density_plot_${direc}.png 
done
cd /projects/jnorhos/plumberg/CausalityChecker


for direc in ../OSU_hydro/RESULTS_pPb_OPTIMAL_nc6 ../OSU_hydro/test_all
do
	python3 plot_hyperbol_viol_vs_tau_e.py 0 ${direc}/char_vel_frames/*
done

cp ../OSU_hydro/test_all/hyperbol_viol_density_plot.png \
   ../OSU_hydro/test_all/hyperbol_viol_density_plot_PbPb_VISHNU.png

cp ../OSU_hydro/RESULTS_pPb_OPTIMAL_nc6/hyperbol_viol_density_plot.png \
   ../OSU_hydro/RESULTS_pPb_OPTIMAL_nc6/hyperbol_viol_density_plot_pPb_VISHNU.png
