#!/usr/bin/env bash
#------------------

cwd=`pwd`

filePath=`readlink -e $1`
fileDirec=`dirname $filePath`
fileName=`basename $filePath`

eDec=$4

frameDirName=char_vel_frames
slideDirName=char_vel_slides
frameStem=frame_w_char_vel
slideStem=slide_w_char_vel

(
	cd $fileDirec
	rm -rf $frameDirName $slideDirName characteristic_velocity_evolution.mp4
	mkdir $frameDirName
	mkdir $slideDirName

	# assuming same number of lines for each tau...
	split --lines=$3 -d --suffix-length=4 $fileName $frameDirName/${frameStem}
	nFiles=`\ls -1 $frameDirName/${frameStem}* | wc -l`

	for i in $(seq -f "%04g" $nFiles $[nFiles+10])
	do
		echo > $frameDirName/${frameStem}${i}
	done
	for file in $frameDirName/${frameStem}*
	do
		mv $file $file".dat"
	done
)

	# Get total number of frames
	i=`\ls -1 $fileDirec/$frameDirName/${frameStem}* | wc -l`

	# This generates frames for the animations of the characteristic velocities
	echo 'Executing python generate_char_vel_frames.py '$2' 0 '$i' '$fileDirec"/$frameDirName "$fileDirec"/$slideDirName" $4 $5
	python generate_char_vel_frames.py $2 0 $i $fileDirec/$frameDirName $fileDirec/$slideDirName $4 $5

(
	cd $fileDirec
	framesPerSecond=60
	pngs2mp4 $framesPerSecond $slideDirName/${slideStem}%04d.png characteristic_velocity_evolution.mp4
)
