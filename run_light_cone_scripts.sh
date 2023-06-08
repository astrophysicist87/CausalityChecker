#!/usr/bin/env bash
#SBATCH -t 16:00:00
#SBATCH -A qgp
#SBATCH -p qgp

bash generate_light_cone_plots.sh ../MUSIC/v8_bugfix_def_chi0_10/PbPb_noKompost/results/ $[512**2]
