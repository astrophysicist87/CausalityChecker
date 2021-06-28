#!/bin/bash
#SBATCH -t 16:00:00                # Job run time (hh:mm:ss)
#SBATCH -N 1                       # Number of nodes
#SBATCH -J serial_job              # Name of batch job
#SBATCH -A qgp
#SBATCH -p qgp
#SBATCH -o serial.o%j              # Name of batch job output file
#SBATCH -e serial.e%j              # Name of batch job output file

outfile=`dirname $file_to_check`/causality_check_w_characteristic_velocities.dat
errfile=`dirname $file_to_check`/causality_check_w_characteristic_velocities.err

if [ ! -f "$outfile" ]
then
	./check_causality_3_plus_1D $file_to_check 1> $outfile 2> $errfile
else
	echo "$outfile already exists"'!!!'
fi

